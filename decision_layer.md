# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-26T04:58:13.036853+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : DOT-EUR | action ACHETE_MAINTENANT | opportunité 9.306 | entrée 7.350 | trend 8.450 | rang 8.374
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : RPL-EUR | action PLACE_LIMITE_PASSIVE | opportunité 9.381 | entrée 6.100 | trend 9.000 | rang 8.324
  - Strong structure but imperfect current entry; prefer passive execution. High extension/chase reduces rank but does not erase the setup.
- **MEILLEUR_LATENT_ACCELERATOR** : APT-EUR | action LATENT_ACCELERATOR | opportunité 8.412 | entrée 5.650 | trend 8.950 | rang 7.940
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : FET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.445 | entrée 8.300 | trend 8.850 | rang 8.478
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.478
2. DOT-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.374
3. KAS-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.355

## Accélération indépendante

- ACE-EUR — CONFIRMED_ACCELERATION — score 8.136/10 — DETECTED_BUT_TOO_LATE
- VET-EUR — CONFIRMED_ACCELERATION — score 7.320/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PEAQ-EUR — BUILDING_ACCELERATION — score 6.364/10 — DETECTED_BUT_TOO_LATE
- ENA-EUR — BUILDING_ACCELERATION — score 5.884/10 — DETECTED_BUT_TOO_LATE
- PUMP-EUR — BUILDING_ACCELERATION — score 5.784/10 — DETECTED_BUT_TOO_LATE
- SAGA-EUR — BUILDING_ACCELERATION — score 5.556/10 — DETECTED_BUT_TOO_LATE
- GRASS-EUR — BUILDING_ACCELERATION — score 5.448/10 — DETECTED_BUT_TOO_LATE
- FET-EUR — BUILDING_ACCELERATION — score 5.212/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- KAS-EUR — ACTIVE_NOW — score mémoire 8.355/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- VET-EUR — ACTIVE_NOW — score mémoire 8.206/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- POND-EUR — MEMORY_24H — score mémoire 9.585/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 9.578/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 9.118/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 8.896/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CTC-EUR — MEMORY_24H — score mémoire 8.874/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ONT-EUR — MEMORY_24H — score mémoire 8.859/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WIN-EUR — MEMORY_24H — score mémoire 8.694/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FET-EUR — ACTIVE_NOW — score mémoire 8.478/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- POND-EUR +106.55% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PHA-EUR +68.81% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- ARK-EUR +31.92% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AERO-EUR +26.18% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ENA-EUR +25.67% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SAGA-EUR +22.27% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SEI-EUR +18.05% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RARE-EUR +16.75% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KMNO-EUR +16.57% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- JTO-EUR +16.55% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
