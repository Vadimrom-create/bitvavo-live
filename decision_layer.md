# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-26T11:23:35.238178+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LINK-EUR | action ACHETE_MAINTENANT | opportunité 9.422 | entrée 8.250 | trend 8.750 | rang 8.637
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ROSE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.297 | entrée 5.800 | trend 8.700 | rang 7.774
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : DUSK-EUR | action LATENT_ACCELERATOR | opportunité 8.208 | entrée 5.600 | trend 8.700 | rang 7.742
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ZK-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.901 | entrée 6.300 | trend 8.700 | rang 8.099
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. LINK-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.637
2. ALGO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.478
3. ICP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.455

## Accélération indépendante

- WMTX-EUR — CONFIRMED_ACCELERATION — score 9.000/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SWELL-EUR — CONFIRMED_ACCELERATION — score 6.646/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- UMA-EUR — BUILDING_ACCELERATION — score 6.326/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PEAQ-EUR — BUILDING_ACCELERATION — score 5.840/10 — DETECTED_BUT_TOO_LATE
- LMWR-EUR — BUILDING_ACCELERATION — score 5.634/10 — DETECTED_BUT_TOO_LATE
- GOAT-EUR — BUILDING_ACCELERATION — score 5.409/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HNT-EUR — BUILDING_ACCELERATION — score 5.286/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DYDX-EUR — BUILDING_ACCELERATION — score 5.141/10 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — BUILDING_ACCELERATION — score 5.050/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GLMR-EUR — BUILDING_ACCELERATION — score 4.985/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- OP-EUR — ACTIVE_NOW — score mémoire 7.939/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- W-EUR — ACTIVE_NOW — score mémoire 7.904/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- GALA-EUR — ACTIVE_NOW — score mémoire 7.864/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ZRC-EUR — MEMORY_24H — score mémoire 9.830/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 9.578/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WMTX-EUR — ACTIVE_NOW — score mémoire 9.000/10 — sources ACCELERATION — WATCH_ONLY
- CTC-EUR — MEMORY_24H — score mémoire 8.874/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ONT-EUR — MEMORY_24H — score mémoire 8.859/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- LINK-EUR — ACTIVE_NOW — score mémoire 8.637/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ACT-EUR — MEMORY_24H — score mémoire 8.555/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- POND-EUR +151.75% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +84.15% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- 2Z-EUR +33.17% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- PHA-EUR +27.30% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PROM-EUR +21.02% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- ENA-EUR +19.06% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AERO-EUR +15.45% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARK-EUR +15.24% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TNSR-EUR +13.62% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- KMNO-EUR +12.49% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
