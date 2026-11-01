# TCCC Evaluation Suite — v3.0.1 Android / APK

**Release:** v3.0.1  
**Android versionCode:** 30000  
**Role:** Offline TCCC field evaluation, local training management, readiness analytics, and program oversight

v3.0.1 is a maintenance release on the field-driven usability and information-architecture release built directly from the validated **v2.21.2** baseline. It preserves the existing Tier 1–4 curriculum/checklist content, timers, scoring thresholds, critical-failure logic, RCA/performance-intelligence data, MAJCOM/base metadata, local persistence, reports, exports, backup/restore, branding, and Android build pipeline unless specifically changed below.

## Major v3.0 changes

### OBSERVE | REVIEW
The prior Field Mode / Review Mode interface is now a clear segmented **OBSERVE | REVIEW** control.

**OBSERVE** prioritizes live grading:
- student / attempt,
- phase and current unresolved criterion,
- PASS / FAIL / NT,
- active timers,
- critical-failure warning,
- current score and unresolved count,
- Next Unresolved,
- phase navigation.

It minimizes review/admin material such as source citations, timeline, notes, sign-off, failure-analysis summaries, and export/finalization controls.

**REVIEW** restores the existing detailed information and administrative functions, including source information, failure details, notes, timeline/history, sign-off, finalization, and individual exports.

### PASS | FAIL | NT only
N/O is removed as a selectable grade. A criterion with no grade is **blank/unresolved** and blocks finalization when required.

Legacy saved `N/O` values are migrated safely to blank/unresolved. The original legacy value is retained under migration metadata (`legacyRatings`) for auditability rather than being silently treated as PASS/FAIL/NT.

### Simplified failure classification
Evaluator-facing failure modes are:
- Omitted
- Incorrect
- Delayed / Wrong Sequence
- Incomplete
- Unsafe / Other

Primary Root Cause is renamed **Primary Performance Contributor**, with:
- Knowledge
- Recognition / Judgment
- Skill / Execution
- Prioritization / Teamwork
- Environment / System

Analytics now use **Observed Performance Contributors** language. These are evaluator observations, not scientific causal determinations.

### Readable operational interface
Operational typography and control sizing were increased. PASS / FAIL / NT controls use a three-column layout, criteria remain readable on phones/tablets, and responsive rules prevent text clipping/overflow or uncontrolled button height.

### Performance versus exposure
NT remains excluded from the student performance denominator. Analytics separately show:
- performance when tested,
- tested/exposure rate,
- NT rate.

A high NT percentage is therefore not presented as successful performance.

### Cleaner exports
The primary class action is **Export Class Summary**. All existing detailed exports remain available under **More Exports ▾**, including summary, criteria, timer, event/audit, performance analytics, enterprise detail, and backup JSON.

### Simplified startup disclosure
The opening screen prominently presents:
- **TRAINING USE ONLY**
- **NO PHI/CUI**
- **DATA STORED LOCALLY**

Detailed safeguards remain available under **View Safeguards** and are not removed.

### Four-area information architecture
Home functions are organized into:
- **EVALUATE**
- **MANAGE TRAINING**
- **READINESS**
- **PROGRAM**

No cloud, authentication, API, or enterprise backend is added.

## Offline/local architecture
The evaluator remains local/offline-first. There is no network transport in app logic, and the Content Security Policy retains `connect-src 'none'`.

Working records remain in local device storage. Existing local PDF/CSV/JSON export functionality remains available through the Android filesystem layer.

## Future-sync preparation — local only
v3.0 adds local future-ready metadata without transmitting anything:
- stable class / participant / attempt IDs,
- parent linkage (`classId`, `participantId`),
- device-generated identifier,
- created / modified timestamps,
- application version,
- content/curriculum version,
- `syncStatus: "LOCAL"`.

The data model can later support states such as LOCAL / PENDING / SYNCED / CONFLICT, but **v3.0 performs no synchronization and transmits no records**.

## Preserved from v2.21.2
- CUF → EVAC workflow
- Tier 1 ASM / Tier 2 CLS / Tier 3 CMC / Tier 4 CPP
- 75% scoring threshold and critical-failure override
- current TCCC criterion content/order/criticality/source references
- all 22 timer definitions
- cross-phase Active Timers STOP controls
- top CUF Tourniquet quick timer
- overall TTA timers on all four tiers
- wound-packing and advanced CMC/CPP timers
- Next Unresolved top and bottom
- scenario NT setup and NT justification
- A1/A2 remediation behavior
- class locking/finalization
- local records
- class/readiness/program analytics
- MAJCOM/base metadata
- curriculum/version snapshots
- PDF/CSV exports
- backup/restore
- TCCC icon/splash branding
- approved tourniquet wording: **“Wound could be closely monitored.”**
- **Contact: John Garcia** only

## Validation
See:
- `FIELD_FEEDBACK_IMPLEMENTATION_v3.0.0.md`
- `VALIDATION_REPORT_v3.0.0.md`
- `CHANGELOG-v3.0.0.md`

## Build test APK
1. Place this repository contents at the root of the APK GitHub repository.
2. Open **Actions**.
3. Run **Build TCCC Test APK**.
4. Download **`TCCC-v3.0.1-test.apk`**.

The Android project is generated during CI, then TCCC launcher/splash resources are reapplied and Android hardening/versioning is verified before Gradle builds.

## Signed release
Use **Build TCCC Signed Release APK** after the repository signing secrets are configured. Do not commit a keystore or passwords.

**Contact: John Garcia**
