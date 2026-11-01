// Apply the RaPS version and security settings to the generated Android project.
// - versionName = RaPS version (e.g. 3.4.13-web.5)
// - versionCode = RaPS versionCode x 100 + web number, so it always increases
// - backups and cleartext traffic disabled
// - INTERNET permission kept: the app signs in and syncs with the RaPS server
import fs from 'node:fs';
import path from 'node:path';

const versionSource = fs.readFileSync(path.resolve('www/version.js'), 'utf8');
const name = versionSource.match(/versionName:\s*['"]([^'"]+)['"]/)?.[1];
const baseCode = Number(versionSource.match(/versionCode:\s*(\d+)/)?.[1]);
if (!name || !baseCode) throw new Error('Could not read versionName/versionCode from www/version.js');
const webNumber = Number(name.match(/web\.(\d+)/)?.[1] ?? 0);
if (webNumber > 99) throw new Error(`web number ${webNumber} does not fit the versionCode scheme`);
const code = baseCode * 100 + webNumber;

const manifestPath = path.resolve('android/app/src/main/AndroidManifest.xml');
let manifest = fs.readFileSync(manifestPath, 'utf8');
for (const [attr, value] of [['allowBackup', 'false'], ['fullBackupContent', 'false'], ['usesCleartextTraffic', 'false']]) {
  const re = new RegExp(`android:${attr}="[^"]*"`);
  manifest = re.test(manifest)
    ? manifest.replace(re, `android:${attr}="${value}"`)
    : manifest.replace(/<application\b/, `<application android:${attr}="${value}"`);
}
if (!manifest.includes('android.permission.INTERNET')) {
  manifest = manifest.replace(/<manifest\b[^>]*>/, (m) => `${m}\n    <uses-permission android:name="android.permission.INTERNET" />`);
}
fs.writeFileSync(manifestPath, manifest);

const gradlePath = path.resolve('android/app/build.gradle');
let gradle = fs.readFileSync(gradlePath, 'utf8');
gradle = gradle.replace(/versionCode\s+\d+/, `versionCode ${code}`).replace(/versionName\s+["'][^"']*["']/, `versionName "${name}"`);
if (!gradle.includes(`versionCode ${code}`) || !gradle.includes(`versionName "${name}"`)) {
  throw new Error('Could not set the version in android/app/build.gradle');
}
fs.writeFileSync(gradlePath, gradle);

if (process.env.GITHUB_OUTPUT) {
  fs.appendFileSync(process.env.GITHUB_OUTPUT, `name=${name}\ncode=${code}\n`);
}
console.log(`Android hardened: RaPS ${name} (versionCode ${code}); backups and cleartext disabled; INTERNET kept for sync.`);
