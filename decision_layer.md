# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T00:49:51.597882+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : TAO-EUR | action ACHETE_MAINTENANT | opportunité 8.050 | entrée 7.400 | trend 8.250 | rang 7.667
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : PEPE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.782 | entrée 6.700 | trend 8.450 | rang 7.587
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : INJ-EUR | action LATENT_ACCELERATOR | opportunité 7.718 | entrée 5.450 | trend 7.900 | rang 6.302
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ONDO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.967 | entrée 7.000 | trend 8.450 | rang 7.735
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ONDO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.735
2. SUI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.707
3. TAO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.667

## Accélération indépendante

- CELR-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- AVAX-EUR — BUILDING_ACCELERATION — score 5.755/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CELR-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- MIOTA-EUR — ACTIVE_NOW — score mémoire 8.100/10 — sources V4 — WATCH_ONLY
- APT-EUR — ACTIVE_NOW — score mémoire 8.073/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- HYPE-EUR — ACTIVE_NOW — score mémoire 8.036/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- RED-EUR — ACTIVE_NOW — score mémoire 7.967/10 — sources V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 7.941/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- IMX-EUR — ACTIVE_NOW — score mémoire 7.923/10 — sources V4 — WATCH_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.918/10 — sources V4 — WATCH_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 7.901/10 — sources V4 — WATCH_ONLY
- SUPER-EUR — ACTIVE_NOW — score mémoire 7.869/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CELR-EUR +83.39% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +48.18% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZAMA-EUR +29.87% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AVAX-EUR +27.42% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ENA-EUR +22.02% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- XTZ-EUR +21.29% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIL-EUR +19.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- INJ-EUR +19.74% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SKL-EUR +16.95% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +16.36% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
