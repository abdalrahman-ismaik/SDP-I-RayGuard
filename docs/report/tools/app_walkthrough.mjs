// Capture RayGuard-App walkthrough screenshots from real runs (see ../README.md).
// Run from the app's frontend folder, which provides Playwright; needs installed Chrome.
import { chromium } from 'playwright'
const args = process.argv.slice(2)
const modelOnly = args[0] === '--model' && Boolean(args.shift())
const [out, data, scan, ...rest] = args
const base = 'http://127.0.0.1:8771'
const b = await chromium.launch({ channel: 'chrome' })
const p = await b.newPage({ viewport: { width: 1360, height: 850 }, deviceScaleFactor: 2, reducedMotion: 'reduce' })
p.setDefaultTimeout(20000)
const shot = n => p.screenshot({ path: `${out}/${n}.png` })
if (modelOnly) await captureModel(); else await captureWalkthrough()

async function captureWalkthrough() {
await p.goto(base + '/#inspect')
await p.getByRole('button', { name: 'Switch to light mode' }).click().catch(e => console.log('light', e.message.slice(0, 80)))
await p.getByText('Appearance', { exact: true }).click()
console.log(await p.getByRole('radio').evaluateAll(r => r.map(x => x.getAttribute('aria-label') || x.parentElement.innerText)))
await p.getByRole('radio', { name: /Barlow/ }).check().catch(e => console.log('font', e.message.slice(0, 300)))
await p.getByRole('button', { name: 'Close appearance' }).click()
const nav = n => p.getByRole('navigation', { name: 'Workspace sections' }).getByRole('link', { name: n, exact: true }).click()
await nav('Workspace setup'); await p.waitForTimeout(800); await shot('1-setup')
await nav('Inspect'); await p.getByLabel('Upload X-ray image').setInputFiles(data + '/' + scan)
await p.waitForTimeout(1500); await shot('2-loaded')
await p.getByRole('button', { name: 'Run inference', exact: true }).click()
await p.waitForTimeout(1500); await shot('3-processing')
await p.getByText('Select a finding to locate it').or(p.getByText('No detections reported')).or(p.getByText('Inference did not complete')).first().waitFor({ timeout: 180000 })
await p.waitForTimeout(1000); await shot('4-result')
await p.getByRole('tab', { name: 'Provenance', exact: true }).click(); await p.waitForTimeout(500); await shot('5-provenance')
await p.getByRole('tab', { name: 'Review', exact: true }).click()
await p.getByLabel('Review note').fill('Localized region inspected; refer for manual check.')
await p.getByRole('button', { name: 'Flag for follow-up' }).click(); await p.waitForTimeout(1200); await shot('6-review')
const idx = rest.map(Number)
for (const i of idx) {
  const r = await p.evaluate(async i => (await fetch('/api/demo', { method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify({ action: 'start', start_index: i, count: 1, confidence: 0.25 }) })).json(), i)
  console.log(i, r.state, r.next_name || r.detail && JSON.stringify(r.detail))
  for (let k = 0; k < 90; k++) { await p.waitForTimeout(2000); const d = await p.evaluate(async () => (await fetch('/api/demo')).json()); if (d.state !== 'running') break }
  await nav('Session'); await p.waitForTimeout(2500)
  await p.getByRole('region', { name: 'Session history', exact: true }).getByRole('button', { name: /Open run/ }).first().click()
  await p.waitForTimeout(2500)
  await p.getByRole('tab', { name: 'Findings', exact: true }).click(); await p.waitForTimeout(800)
  await shot(`7-demo-${i}`)
}
await nav('Session'); await p.waitForTimeout(1000); await shot('8-session')
await b.close()
}

async function captureModel() {
await p.goto(base + '/#inspect')
await p.getByRole('button', { name: 'Switch to light mode' }).click()
await p.getByText('Appearance', { exact: true }).click()
await p.getByRole('radio', { name: /Barlow/ }).check(); await p.getByRole('button', { name: 'Close appearance' }).click()
await p.getByLabel('Upload X-ray image').setInputFiles(data + '/' + scan)
await p.waitForTimeout(1500)
const run = p.getByRole('button', { name: 'Run inference', exact: true })
const nav = n => p.getByRole('navigation', { name: 'Workspace sections' }).getByRole('link', { name: n, exact: true }).click()
await nav('Source'); await p.waitForTimeout(800)
console.log((await p.getByRole('button').allTextContents()).join(' | '))
await p.getByRole('button', { name: /verify/i }).first().click()
for (let k = 0; k < 90; k++) { await p.waitForTimeout(2000); const r = await p.evaluate(async () => (await (await fetch('/api/health')).json()).runtime); if (r.state !== 'verifying') { console.log(r.state, r.reason, r.error); break } }
await nav('Inspect'); await p.waitForTimeout(2500)
await run.click()
await p.getByText('Select a finding to locate it').or(p.getByText('No detections reported')).or(p.getByText('Inference did not complete')).first().waitFor({ timeout: 180000 })
await p.waitForTimeout(1000); await p.screenshot({ path: `${out}/9-${rest[0]}.png` }); await b.close()
}
