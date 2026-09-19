# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T23:19:31.775862+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : TAO-EUR | action ACHETE_MAINTENANT | opportunité 8.066 | entrée 7.450 | trend 8.250 | rang 7.766
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.449 | entrée 6.550 | trend 8.700 | rang 7.865
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.865
2. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.854
3. TAO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.766

## Accélération indépendante

- G-EUR — CONFIRMED_ACCELERATION — score 8.451/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- G-EUR — ACTIVE_NOW — score mémoire 8.451/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- NPC-EUR — ACTIVE_NOW — score mémoire 8.153/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 8.059/10 — sources V4 — WATCH_ONLY
- JUP-EUR — ACTIVE_NOW — score mémoire 8.042/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- POL-EUR — ACTIVE_NOW — score mémoire 8.037/10 — sources ACCELERATION, V4 — WATCH_ONLY
- RUNE-EUR — ACTIVE_NOW — score mémoire 8.027/10 — sources V4 — WATCH_ONLY
- APT-EUR — ACTIVE_NOW — score mémoire 8.011/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 7.970/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 7.949/10 — sources V4 — WATCH_ONLY
- GRT-EUR — ACTIVE_NOW — score mémoire 7.927/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CELR-EUR +49.75% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZAMA-EUR +41.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- G-EUR +35.36% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- INJ-EUR +25.22% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +23.87% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- XTZ-EUR +23.81% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENA-EUR +21.79% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AVAX-EUR +20.82% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- SKL-EUR +16.50% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- HEI-EUR +13.22% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
