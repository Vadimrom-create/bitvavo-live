# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T14:18:31.124750+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HYPE-EUR | action ACHETE_MAINTENANT | opportunité 8.004 | entrée 8.150 | trend 8.750 | rang 8.037
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : SUI-EUR | action LATENT_ACCELERATOR | opportunité 7.635 | entrée 4.500 | trend 8.200 | rang 7.224
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ONDO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.149 | entrée 8.200 | trend 8.450 | rang 7.787
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.037
2. ONDO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.787
3. SOL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.742

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- ZAMA-EUR — MEMORY_24H — score mémoire 8.324/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.115/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 8.092/10 — sources V4 — WATCH_ONLY
- FLUX-EUR — ACTIVE_NOW — score mémoire 8.073/10 — sources V4 — WATCH_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 8.048/10 — sources V4 — WATCH_ONLY
- HYPE-EUR — ACTIVE_NOW — score mémoire 8.037/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- EIGEN-EUR — ACTIVE_NOW — score mémoire 7.977/10 — sources V4 — WATCH_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 7.950/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KMNO-EUR — ACTIVE_NOW — score mémoire 7.942/10 — sources V4 — WATCH_ONLY
- LPT-EUR — ACTIVE_NOW — score mémoire 7.890/10 — sources ACCELERATION, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZAMA-EUR +44.89% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +35.23% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- XTZ-EUR +31.50% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- STRK-EUR +26.78% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +26.28% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- F-EUR +24.48% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ENA-EUR +22.44% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HEI-EUR +22.30% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +21.66% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- EPIC-EUR +19.03% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
