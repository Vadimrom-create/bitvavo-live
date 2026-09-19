# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T13:33:04.381941+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ONDO-EUR | action ACHETE_MAINTENANT | opportunité 8.221 | entrée 7.600 | trend 8.450 | rang 7.735
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : SOL-EUR | action LATENT_ACCELERATOR | opportunité 7.481 | entrée 4.500 | trend 8.250 | rang 7.191
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : HYPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.831 | entrée 6.950 | trend 8.750 | rang 7.824
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.824
2. ONDO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.735
3. XLM-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.308

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- ONDO-EUR — ACTIVE_NOW — score mémoire 7.735/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- XLM-EUR — ACTIVE_NOW — score mémoire 7.308/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ZAMA-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 8.233/10 — sources V4 — DETECTED_BUT_TOO_LATE
- KMNO-EUR — ACTIVE_NOW — score mémoire 8.066/10 — sources V4 — WATCH_ONLY
- LPT-EUR — ACTIVE_NOW — score mémoire 7.986/10 — sources ACCELERATION, V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.986/10 — sources V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 7.942/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 7.932/10 — sources V4 — WATCH_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 7.878/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZAMA-EUR +39.46% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +38.14% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- EDGE-EUR +32.30% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +32.14% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- HEI-EUR +29.39% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +29.08% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- F-EUR +27.44% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- XTZ-EUR +25.49% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +21.23% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENA-EUR +20.32% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
