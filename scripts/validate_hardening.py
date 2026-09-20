from pathlib import Path
import json, re
root=Path(__file__).resolve().parents[1]; www=root/'www'
def read(p): return p.read_text(encoding='utf-8')
app=read(www/'app.js'); css=read(www/'styles.css'); idx=read(www/'index.html'); tiers=read(www/'tiers.js'); version=read(www/'version.js'); branding=read(www/'branding.js'); installs=read(www/'installations.js'); harden=read(root/'scripts'/'harden-android.mjs')
package=json.loads(read(root/'package.json')); tw=read(root/'.github/workflows/build-test-apk.yml'); rw=read(root/'.github/workflows/build-release-apk.yml')
name=re.search(r"versionName:\s*['\"]([^'\"]+)['\"]",version).group(1); code=int(re.search(r'versionCode:\s*(\d+)',version).group(1))
m=re.search(r'Object\.freeze\((\{[\s\S]*\})\);\s*$',installs); catalog=json.loads(m.group(1)) if m else {}
commands={x['id'] for x in catalog.get('commands',[])}; bases=catalog.get('installations',[]); ids=[x.get('id') for x in bases]
struct=all(x.get('id') and x.get('name') and x.get('hostCommand') and isinstance(x.get('commands'),list) for x in bases)
refs=all(x.get('hostCommand') in commands and all(c in commands for c in x.get('commands',[])) for x in bases)
checks={
'authoritative version 3.0.1': name=='3.0.1' and code==30001,
'package version matches': package.get('version')==name,
'database schema v5': 'x.schemaVersion=5' in app and 'db.schemaVersion=5' in app and 'schemaVersion:5' in app,
'future-sync local metadata': all(x in app for x in ['deviceId','createdAt','modifiedAt','lastModifiedDeviceId','syncStatus','SYNC_LOCAL','classId','participantId','appVersion','contentVersion']),
'no network transport added': "connect-src 'none'" in idx and 'fetch(' not in app and 'XMLHttpRequest' not in app,
'legacy N/O migration': "if(rating==='no')" in app and 'legacyRatings' in app and 'delete a.ratings[itemId]' in app,
'N/O not selectable': 'N/O' not in idx and '"key": "no"' not in tiers and "t.ratings.map(r=>r.key).join(',') !== 'pass,fail,nt'" in read(root/'scripts'/'validate-content.mjs'),
'blank unresolved blocks finalization': "!st.ratings[i.id]" in app and 'Resolve all required criteria and timing standards before finalization.' in app,
'observe review segmented control': all(x in idx for x in ['observeModeBtn','reviewModeBtn','OBSERVE','REVIEW']) and '.modeSegmented' in css,
'observe mode progressive disclosure': all(x in css for x in ['.observeMode #instructionsCard','.observeMode #reviewTimelineCard','.observeMode #reviewSignoffCard','.observeMode .failureSummary','.observeMode .noteToggle']),
'review mode preserves detail': '.reviewMode #instructionsCard' in css and '.reviewMode #reviewTimelineCard' in css and 'Sign-Off / Notes' in idx,
'operational type size': '.itemText{font-size:16px' in css and '.choice{font-size:15px' in css and '.kpis small,#evalHeader.collapsed .kpis small{font-size:12px!important' in css and '.crit,.localBadge,.sourceBadge,.noteBadge,.forcedBadge{font-size:12px}' in css,
'3-state grading layout': '.choices{grid-template-columns:repeat(3' in css,
'failure modes simplified': all(x in app for x in ["['omitted','Omitted']","['incorrect','Incorrect']","['delayed-sequence','Delayed / Wrong Sequence']","['incomplete','Incomplete']","['unsafe-other','Unsafe / Other']"]),
'performance contributor categories simplified': all(x in app for x in ["['knowledge','Knowledge']","['recognition-judgment','Recognition / Judgment']","['skill-execution','Skill / Execution']","['prioritization-teamwork','Prioritization / Teamwork']","['environment-system','Environment / System']"]),
'performance contributor terminology': 'Primary Performance Contributor' in app and 'Observed Performance Contributors' in idx and 'Primary Root Causes' not in idx,
'critical fail contributor requirement retained': 'Critical failures require a Primary Performance Contributor.' in app,
'NT performance vs exposure analytics': all(x in app for x in ['Pass when tested','Fail when tested','g.coverage','g.ntRate']) and 'Scenario coverage' in app,
'exports decluttered without removal': 'Export Class Summary' in idx and 'More Exports' in idx and all(x in idx for x in ['classSummaryCsvBtn','classCriteriaCsvBtn','classTimersCsvBtn','classEventsCsvBtn','classAnalyticsCsvBtn','classEnterpriseCsvBtn','backupClassBtn']),
'safety disclosure simplified': all(x in idx for x in ['TRAINING USE ONLY','NO PHI/CUI','DATA STORED LOCALLY','View Safeguards','Acknowledge &amp; Continue']),
'four-area information architecture': all(x in idx for x in ['EVALUATE','MANAGE TRAINING','READINESS','PROGRAM','areaEvaluate','areaManage','areaReadiness','areaProgram']),
'information architecture navigation logic': 'setHomeArea' in app and 'data-home-area' in idx,
'installation catalog loads before app': idx.find('installations.js')>0 and idx.find('installations.js')<idx.find('app.js'),
'installation catalog stable': len(bases)>=70 and len(ids)==len(set(ids)) and struct and refs,
'installation tenant relationships retained': any(len(x.get('commands',[]))>1 for x in bases),
'MAJCOM/base management retained': all(x in idx for x in ['managementMajcom','managementInstallation','managementTier','managementCourseType','managementMajcomTable','managementInstallationTable']),
'home vs training location retained': 'Training location is the same as home installation' in app and 'trainingLocationType' in app,
'program data quality retained': all(x in app for x in ['classes missing MAJCOM','classes missing home installation','failed observations missing contributor']),
'management summary export retained': 'exportManagementSummaryCsv' in app and 'managementSummaryCsvBtn' in idx,
'analytics schema v3': "TCCC_ANALYTICS_3.0" in app,
'enterprise detail retained': all(x in app for x in ['operational_majcom','home_installation_id','remediation_reason','failure_mode_label','primary_contributor_label']),
'phase status colors retained': '.tab.done{background' in css and '.tab.warn{background' in css,
'next unresolved top/bottom retained': 'id="nextUnresolvedBottomBtn"' in idx and "$('nextUnresolvedBottomBtn').onclick=nextUnresolved" in app,
'contact privacy retained': 'mailto:' not in branding and 'tel:' not in branding and 'Contact: ${b.officeName}' in branding,
'modal fixed': re.search(r'\.modal\{position:fixed;inset:0;z-index:900;.*align-items:center;justify-content:center',css) is not None,
'mass pass remains removed': 'function completeBlock(' not in app,
'NT justification retained': 'NT_REASONS' in app and 'requestNtReason' in app,
'A2 remediation retained': 'Attempt 2 is reserved for remediation' in app and 'remediationReason' in app and 'remediationAction' in app,
'pre-assessment gate retained': 'Evaluator ready check' in app and 'Begin Assessment' in app,
'void unfinished attempt retained': 'function voidCurrentAttempt()' in app,
'timer recovery retained': 'performance.now' in app and 'RECOVERY REQUIRED' in app,
'CSV formula hardening retained': 'function csvValue' in app and '[=+\\-@]' in app,
'Unicode canvas PDF retained': "canvas.toDataURL('image/jpeg'" in app,
'tourniquet CAN wording retained': all(re.search(fr'"id": "{x}"[\s\S]{{0,500}}Wound could be closely monitored',tiers) for x in ['CMC-062','CPP-062']),
'bad tourniquet wording absent': 'Wound could not be closely monitored' not in tiers,
'class analytics retained': all(x in idx for x in ['classAnalyticsKpis','classHeatmap','evaluatorSignals']) and 'renderClassAnalytics' in app,
'criterion rates normalized': 'failRate:tested?fail/tested:null' in app,
'first vs final analytics retained': "['First-pass'" in app and "['Final pass'" in app,
'roster filters retained': 'data-roster-filter="not-started"' in idx and 'data-roster-filter="remediation"' in idx,
'collapsed evaluator header readable': '#evalHeader.collapsed' in css and 'updateEvalHeaderCollapse' in app,
'native branding resources retained': (root/'native-android-res/mipmap-xxxhdpi/ic_launcher.png').is_file(),
'workflows preflight installations': 'test -f www/installations.js' in tw and 'test -f www/installations.js' in rw,
'workflows branding after Capacitor generation': tw.find('npx cap add android')<tw.find('run: bash scripts/apply-android-native-branding.sh') and rw.find('npx cap add android')<rw.find('run: bash scripts/apply-android-native-branding.sh'),
'quick CUF TQ timer retained': 'quickCufTimerCard' in idx and "includes('cuf tourniquet')" in app,
'active timer cross-phase stop retained': 'data-active-timer-stop' in app and "timerAction(b.dataset.activeTimerStop,'stop')" in app,
'TTA timers all four tiers retained': all(x in tiers for x in ['asm_overall','cls_overall','cmc_overall','cpp_overall']),
'CUF TQ timers all four tiers retained': all(x in tiers for x in ['asm_cuf_tq','cls_cuf_tq','cmc_cuf_tq','cpp_cuf_tq']),
'wound pressure timers all four tiers retained': all(x in tiers for x in ['asm_wound_pressure','cls_wound_pressure','cmc_wound_pressure','cpp_wound_pressure']),
'CMC CPP advanced timers retained': all(x in tiers for x in ['cmc_ndc_hold','cmc_hts_admin','cmc_hts_repeat','cmc_neuro_reassess','cpp_ndc_hold','cpp_hts_admin','cpp_hts_repeat','cpp_neuro_reassess','cpp_ketamine_ivio','cpp_analgesia_repeat']),
}
failed=[k for k,v in checks.items() if not v]
for k,v in checks.items(): print(('PASS' if v else 'FAIL')+' - '+k)
if failed: raise SystemExit('\nValidation failed: '+', '.join(failed))
print(f'\n{len(checks)} v3 release checks passed for TCCC v{name} ({code}); {len(bases)} installations / {len(commands)} commands validated.')
