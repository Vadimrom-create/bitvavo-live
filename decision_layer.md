# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T13:46:15.883856+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ONDO-EUR | action ACHETE_MAINTENANT | opportunité 8.033 | entrée 7.350 | trend 8.450 | rang 7.662
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : SOL-EUR | action LATENT_ACCELERATOR | opportunité 7.635 | entrée 4.500 | trend 8.250 | rang 7.262
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : HYPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.025 | entrée 7.650 | trend 8.750 | rang 7.967
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.967
2. NPC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.887
3. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.726

## Accélération indépendante

- NPC-EUR — BUILDING_ACCELERATION — score 5.509/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- AVAX-EUR — BUILDING_ACCELERATION — score 4.782/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- XLM-EUR — ACTIVE_NOW — score mémoire 7.284/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ZAMA-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AIOZ-EUR — MEMORY_24H — score mémoire 8.233/10 — sources V4 — MEMORY_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.199/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- T-EUR — ACTIVE_NOW — score mémoire 8.062/10 — sources ACCELERATION, V4 — WATCH_ONLY
- LPT-EUR — ACTIVE_NOW — score mémoire 8.036/10 — sources ACCELERATION, V4 — WATCH_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 8.016/10 — sources V4 — WATCH_ONLY
- HYPE-EUR — ACTIVE_NOW — score mémoire 7.967/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.914/10 — sources V4 — WATCH_ONLY
- NPC-EUR — ACTIVE_NOW — score mémoire 7.887/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZAMA-EUR +40.14% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +36.20% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- EDGE-EUR +33.64% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +28.25% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- HEI-EUR +27.54% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- F-EUR +27.30% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- XTZ-EUR +26.72% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- STRK-EUR +25.15% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +20.85% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENA-EUR +18.98% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
