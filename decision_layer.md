# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-27T06:42:13.440324+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : TAO-EUR | action ACHETE_MAINTENANT | opportunité 9.247 | entrée 7.600 | trend 8.300 | rang 8.239
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : PIXEL-EUR | action PLACE_LIMITE_PASSIVE | opportunité 9.211 | entrée 6.100 | trend 8.450 | rang 8.207
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ROSE-EUR | action LATENT_ACCELERATOR | opportunité 8.162 | entrée 5.200 | trend 8.950 | rang 7.778
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : KAS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.456 | entrée 7.700 | trend 8.950 | rang 8.304
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. KAS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.304
2. TAO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.239
3. ONDO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.230

## Accélération indépendante

- XMN-EUR — CONFIRMED_ACCELERATION — score 9.365/10 — DETECTED_BUT_TOO_LATE
- GLMR-EUR — CONFIRMED_ACCELERATION — score 8.628/10 — DETECTED_BUT_TOO_LATE
- HFT-EUR — CONFIRMED_ACCELERATION — score 8.107/10 — DETECTED_BUT_TOO_LATE
- POND-EUR — CONFIRMED_ACCELERATION — score 7.861/10 — DETECTED_BUT_TOO_LATE
- DEEP-EUR — CONFIRMED_ACCELERATION — score 7.609/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRO-EUR — CONFIRMED_ACCELERATION — score 7.314/10 — DETECTED_BUT_TOO_LATE
- ENS-EUR — BUILDING_ACCELERATION — score 5.919/10 — DETECTED_BUT_TOO_LATE
- FET-EUR — BUILDING_ACCELERATION — score 5.823/10 — DETECTED_BUT_TOO_LATE
- METIS-EUR — BUILDING_ACCELERATION — score 5.763/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- VET-EUR — BUILDING_ACCELERATION — score 5.704/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- UNI-EUR — ACTIVE_NOW — score mémoire 8.146/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- VET-EUR — ACTIVE_NOW — score mémoire 7.878/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- INX-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- XMN-EUR — ACTIVE_NOW — score mémoire 9.365/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- AGI-EUR — MEMORY_24H — score mémoire 8.644/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GLMR-EUR — ACTIVE_NOW — score mémoire 8.628/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- VELO-EUR — MEMORY_24H — score mémoire 8.605/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AMP-EUR — MEMORY_24H — score mémoire 8.589/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 8.587/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SOON-EUR — MEMORY_24H — score mémoire 8.551/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- QNT-EUR +73.39% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AMP-EUR +36.96% — DETECTED_TOO_LATE — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GLMR-EUR +36.94% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SOON-EUR +35.89% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HFT-EUR +25.31% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- AGI-EUR +20.29% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- W-EUR +19.13% — DETECTED_EARLY — couche NONE — action NONE
- EDGE-EUR +17.85% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RUNE-EUR +17.61% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZRC-EUR +17.20% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
