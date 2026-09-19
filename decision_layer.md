# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T20:22:14.172121+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : SUI-EUR | action ACHETE_MAINTENANT | opportunité 9.041 | entrée 7.950 | trend 8.450 | rang 8.271
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : ONDO-EUR | action LATENT_ACCELERATOR | opportunité 7.570 | entrée 4.500 | trend 7.800 | rang 7.035
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : HYPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.957 | entrée 6.250 | trend 8.750 | rang 7.800
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. SUI-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.271
2. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.800
3. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.156

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- MIOTA-EUR — ACTIVE_NOW — score mémoire 8.418/10 — sources V4 — WATCH_ONLY
- SUI-EUR — ACTIVE_NOW — score mémoire 8.271/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 8.152/10 — sources V4 — WATCH_ONLY
- NEO-EUR — ACTIVE_NOW — score mémoire 8.146/10 — sources V4 — WATCH_ONLY
- LPT-EUR — ACTIVE_NOW — score mémoire 8.114/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 8.089/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ACH-EUR — ACTIVE_NOW — score mémoire 8.063/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 7.896/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- JUP-EUR — ACTIVE_NOW — score mémoire 7.872/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- 0G-EUR — ACTIVE_NOW — score mémoire 7.863/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZAMA-EUR +43.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +40.11% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- EPIC-EUR +38.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +30.61% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- G-EUR +29.12% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CELR-EUR +28.72% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ENA-EUR +22.38% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +20.74% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- INJ-EUR +19.15% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AVAX-EUR +17.72% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
