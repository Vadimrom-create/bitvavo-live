# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-25T15:54:19.368896+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LTC-EUR | action ACHETE_MAINTENANT | opportunité 8.183 | entrée 6.900 | trend 8.650 | rang 7.918
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : MOVR-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.208 | entrée 5.900 | trend 8.950 | rang 7.840
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : CAKE-EUR | action LATENT_ACCELERATOR | opportunité 7.801 | entrée 5.200 | trend 8.950 | rang 7.675
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : PYTH-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.084 | entrée 7.250 | trend 8.950 | rang 8.380
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. PYTH-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.380
2. MANA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.104
3. LTC-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.918

## Accélération indépendante

- RARE-EUR — CONFIRMED_ACCELERATION — score 7.445/10 — DETECTED_BUT_TOO_LATE
- TLM-EUR — CONFIRMED_ACCELERATION — score 7.176/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SPK-EUR — BUILDING_ACCELERATION — score 5.220/10 — DETECTED_BUT_TOO_LATE
- PROM-EUR — BUILDING_ACCELERATION — score 4.898/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- PYTH-EUR — ACTIVE_NOW — score mémoire 8.380/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- HFT-EUR — MEMORY_DECAY_24_72H — score mémoire 8.171/10 — sources ACCELERATION — MEMORY_ONLY
- MANA-EUR — ACTIVE_NOW — score mémoire 8.104/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- REQ-EUR — MEMORY_24H — score mémoire 8.033/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LTC-EUR — ACTIVE_NOW — score mémoire 7.918/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AXS-EUR — ACTIVE_NOW — score mémoire 7.899/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- MOVR-EUR — ACTIVE_NOW — score mémoire 7.840/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AUDIO-EUR — MEMORY_24H — score mémoire 7.821/10 — sources ACCELERATION — MEMORY_ONLY
- ALGO-EUR — ACTIVE_NOW — score mémoire 7.811/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LINK-EUR — ACTIVE_NOW — score mémoire 7.804/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- PHA-EUR +44.95% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- TREAD-EUR +37.23% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RARE-EUR +36.28% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARK-EUR +27.02% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +19.74% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRASS-EUR +16.06% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- QNT-EUR +15.28% — DETECTED_EARLY — couche NONE — action NONE
- KMNO-EUR +14.88% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DBR-EUR +13.83% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ENA-EUR +13.51% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
