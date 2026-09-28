# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-28T05:23:29.754307+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : KAS-EUR | action ACHETE_MAINTENANT | opportunité 8.293 | entrée 7.250 | trend 8.550 | rang 7.901
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : CC-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.081 | entrée 6.100 | trend 9.000 | rang 7.869
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ELSA-EUR | action LATENT_ACCELERATOR | opportunité 7.828 | entrée 5.450 | trend 8.550 | rang 7.516
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : LRC-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.968 | entrée 6.350 | trend 8.000 | rang 7.935
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. KAS-EUR — ACHETE_MAINTENANT — rank 7.901 — opportunité 8.293 — entrée 7.250 — trend 8.550
2. ONDO-EUR — ACHETE_MAINTENANT — rank 7.561 — opportunité 8.062 — entrée 6.950 — trend 8.150

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. LRC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.935
2. KAS-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.901
3. CC-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.869

## Accélération indépendante

- AUDIO-EUR — CONFIRMED_ACCELERATION — score 8.535/10 — DETECTED_BUT_TOO_LATE
- XMN-EUR — CONFIRMED_ACCELERATION — score 8.447/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SOON-EUR — CONFIRMED_ACCELERATION — score 7.236/10 — DETECTED_BUT_TOO_LATE
- XDC-EUR — BUILDING_ACCELERATION — score 6.108/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AZTEC-EUR — BUILDING_ACCELERATION — score 5.105/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TREAD-EUR — BUILDING_ACCELERATION — score 5.057/10 — DETECTED_BUT_TOO_LATE
- ALT-EUR — BUILDING_ACCELERATION — score 4.913/10 — DETECTED_BUT_TOO_LATE
- BIRB-EUR — BUILDING_ACCELERATION — score 4.897/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- IRYS-EUR — BUILDING_ACCELERATION — score 4.751/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- KAS-EUR — ACTIVE_NOW — score mémoire 7.901/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ONDO-EUR — ACTIVE_NOW — score mémoire 7.561/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- DGB-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.828/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AUDIO-EUR — ACTIVE_NOW — score mémoire 8.535/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- XMN-EUR — ACTIVE_NOW — score mémoire 8.447/10 — sources ACCELERATION, V4 — WATCH_ONLY
- FRAX-EUR — MEMORY_24H — score mémoire 8.380/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ACX-EUR — MEMORY_24H — score mémoire 8.120/10 — sources ACCELERATION — MEMORY_ONLY
- CAP-EUR — MEMORY_24H — score mémoire 7.967/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LRC-EUR — ACTIVE_NOW — score mémoire 7.935/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +35.90% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +28.10% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AUDIO-EUR +27.14% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRT-EUR +18.72% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PUMP-EUR +18.02% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOON-EUR +15.05% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- IRYS-EUR +13.33% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- SEI-EUR +12.20% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOSO-EUR +10.41% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- GRASS-EUR +9.99% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
