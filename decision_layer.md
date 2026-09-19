# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T05:30:40.867954+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LINK-EUR | action ACHETE_MAINTENANT | opportunité 8.604 | entrée 7.350 | trend 5.450 | rang 6.947
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : HYPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.677 | entrée 6.100 | trend 8.250 | rang 7.468
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.468
2. ENA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.332
3. APT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.153

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- AAVE-EUR — ACTIVE_NOW — score mémoire 8.222/10 — sources ACCELERATION, V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.997/10 — sources V4 — WATCH_ONLY
- RAY-EUR — ACTIVE_NOW — score mémoire 7.967/10 — sources ACCELERATION, V4 — WATCH_ONLY
- SENT-EUR — ACTIVE_NOW — score mémoire 7.950/10 — sources V4 — DETECTED_BUT_TOO_LATE
- PENDLE-EUR — ACTIVE_NOW — score mémoire 7.919/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- NPC-EUR — ACTIVE_NOW — score mémoire 7.843/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SSV-EUR — ACTIVE_NOW — score mémoire 7.843/10 — sources V4 — WATCH_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 7.811/10 — sources V4 — WATCH_ONLY
- BEAM-EUR — ACTIVE_NOW — score mémoire 7.789/10 — sources V4 — WATCH_ONLY
- T-EUR — ACTIVE_NOW — score mémoire 7.774/10 — sources ACCELERATION, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- G-EUR +62.66% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CPOOL-EUR +35.87% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- F-EUR +35.07% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +32.62% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +29.93% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +24.79% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZIG-EUR +20.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZAMA-EUR +20.26% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +18.77% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- C-EUR +18.61% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
