# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-26T11:39:47.784270+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LINK-EUR | action ACHETE_MAINTENANT | opportunité 9.422 | entrée 8.150 | trend 8.750 | rang 8.591
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : LDO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.931 | entrée 6.000 | trend 8.950 | rang 8.184
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ZK-EUR | action LATENT_ACCELERATOR | opportunité 8.058 | entrée 5.700 | trend 8.700 | rang 7.726
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ATH-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.046 | entrée 6.650 | trend 8.750 | rang 8.211
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. LINK-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.591
2. ALGO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.358
3. TIA-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.286

## Accélération indépendante

- TLM-EUR — CONFIRMED_ACCELERATION — score 9.175/10 — DETECTED_BUT_TOO_LATE
- SFP-EUR — CONFIRMED_ACCELERATION — score 8.674/10 — DETECTED_BUT_TOO_LATE
- SWELL-EUR — CONFIRMED_ACCELERATION — score 7.114/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HNT-EUR — BUILDING_ACCELERATION — score 6.163/10 — DETECTED_BUT_TOO_LATE
- KMNO-EUR — BUILDING_ACCELERATION — score 5.910/10 — DETECTED_BUT_TOO_LATE
- MAV-EUR — BUILDING_ACCELERATION — score 5.863/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ALICE-EUR — BUILDING_ACCELERATION — score 5.505/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AIXBT-EUR — BUILDING_ACCELERATION — score 5.386/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PYTH-EUR — BUILDING_ACCELERATION — score 5.365/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AMP-EUR — BUILDING_ACCELERATION — score 5.346/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- JUP-EUR — ACTIVE_NOW — score mémoire 8.269/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- AVAX-EUR — ACTIVE_NOW — score mémoire 8.016/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ZRC-EUR — MEMORY_24H — score mémoire 9.830/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 9.578/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TLM-EUR — ACTIVE_NOW — score mémoire 9.175/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- WMTX-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION — MEMORY_ONLY
- CTC-EUR — MEMORY_24H — score mémoire 8.874/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ONT-EUR — MEMORY_24H — score mémoire 8.859/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SFP-EUR — ACTIVE_NOW — score mémoire 8.674/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- LINK-EUR — ACTIVE_NOW — score mémoire 8.591/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- POND-EUR +177.40% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +72.36% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PHA-EUR +29.95% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- 2Z-EUR +29.95% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- PROM-EUR +21.20% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- ENA-EUR +15.25% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KMNO-EUR +14.59% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AERO-EUR +14.38% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TLM-EUR +14.07% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARK-EUR +13.83% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
