# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-26T08:45:20.275037+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ADA-EUR | action ACHETE_MAINTENANT | opportunité 8.960 | entrée 7.400 | trend 8.750 | rang 8.372
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : SAFE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.162 | entrée 6.000 | trend 8.750 | rang 7.820
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : LDO-EUR | action LATENT_ACCELERATOR | opportunité 8.154 | entrée 5.550 | trend 8.950 | rang 7.877
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ORCA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.200 | entrée 5.750 | trend 8.450 | rang 8.187
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ADA-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.372
2. KAS-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.286
3. PYTH-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.250

## Accélération indépendante

- XPL-EUR — CONFIRMED_ACCELERATION — score 9.254/10 — DETECTED_BUT_TOO_LATE
- ENJ-EUR — CONFIRMED_ACCELERATION — score 6.635/10 — DETECTED_BUT_TOO_LATE
- FORM-EUR — CONFIRMED_ACCELERATION — score 6.624/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SENT-EUR — BUILDING_ACCELERATION — score 5.788/10 — DETECTED_BUT_TOO_LATE
- DYM-EUR — BUILDING_ACCELERATION — score 5.711/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HEI-EUR — BUILDING_ACCELERATION — score 5.688/10 — DETECTED_BUT_TOO_LATE
- EUL-EUR — BUILDING_ACCELERATION — score 5.511/10 — DETECTED_BUT_TOO_LATE
- CFG-EUR — BUILDING_ACCELERATION — score 5.496/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- STX-EUR — BUILDING_ACCELERATION — score 5.235/10 — DETECTED_BUT_TOO_LATE
- PUMP-EUR — BUILDING_ACCELERATION — score 5.181/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- FUEL-EUR — MEMORY_24H — score mémoire 9.607/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 9.578/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XPL-EUR — ACTIVE_NOW — score mémoire 9.254/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- ICX-EUR — MEMORY_24H — score mémoire 9.063/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 8.896/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CTC-EUR — MEMORY_24H — score mémoire 8.874/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ONT-EUR — MEMORY_24H — score mémoire 8.859/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ACT-EUR — MEMORY_24H — score mémoire 8.555/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ADA-EUR — ACTIVE_NOW — score mémoire 8.372/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 8.286/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- POND-EUR +124.24% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +63.82% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PHA-EUR +36.18% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- 2Z-EUR +33.18% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ARK-EUR +28.11% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ENA-EUR +25.17% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AERO-EUR +19.91% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KMNO-EUR +16.30% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- REZ-EUR +16.27% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PROM-EUR +16.07% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
