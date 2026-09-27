# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-27T23:47:09.958196+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : RENDER-EUR | action ACHETE_MAINTENANT | opportunité 8.714 | entrée 7.500 | trend 9.200 | rang 8.397
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ATH-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.313 | entrée 6.100 | trend 9.200 | rang 8.068
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : BRETT-EUR | action LATENT_ACCELERATOR | opportunité 8.328 | entrée 5.000 | trend 9.000 | rang 7.857
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : SENT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.228 | entrée 7.100 | trend 8.400 | rang 8.228
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. RENDER-EUR — ACHETE_MAINTENANT — rank 8.397 — opportunité 8.714 — entrée 7.500 — trend 9.200
2. ONDO-EUR — ACHETE_MAINTENANT — rank 8.164 — opportunité 8.644 — entrée 7.650 — trend 8.850
3. TIA-EUR — ACHETE_MAINTENANT — rank 7.965 — opportunité 8.310 — entrée 7.200 — trend 8.650

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. RENDER-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.397
2. SENT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.228
3. ONDO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.164

## Accélération indépendante

- DGB-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- GRASS-EUR — BUILDING_ACCELERATION — score 5.894/10 — DETECTED_BUT_TOO_LATE
- VELO-EUR — BUILDING_ACCELERATION — score 5.662/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- VIRTUAL-EUR — BUILDING_ACCELERATION — score 5.046/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ONDO-EUR — BUILDING_ACCELERATION — score 5.001/10 — DETECTED_BUT_TOO_LATE
- RARE-EUR — BUILDING_ACCELERATION — score 4.803/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- DGB-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- YB-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- QNT-EUR — MEMORY_24H — score mémoire 8.429/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- RENDER-EUR — ACTIVE_NOW — score mémoire 8.397/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FRAX-EUR — MEMORY_24H — score mémoire 8.380/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SENT-EUR — ACTIVE_NOW — score mémoire 8.228/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ONDO-EUR — ACTIVE_NOW — score mémoire 8.164/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ACX-EUR — MEMORY_24H — score mémoire 8.120/10 — sources ACCELERATION — MEMORY_ONLY
- ATH-EUR — ACTIVE_NOW — score mémoire 8.068/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- OP-EUR — ACTIVE_NOW — score mémoire 8.021/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +90.91% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOON-EUR +44.70% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- INX-EUR +30.72% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRT-EUR +28.67% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +22.13% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- W-EUR +20.40% — DETECTED_EARLY — couche NONE — action NONE
- PUMP-EUR +16.80% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- XDC-EUR +15.87% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- IMX-EUR +14.38% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AUDIO-EUR +13.15% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
