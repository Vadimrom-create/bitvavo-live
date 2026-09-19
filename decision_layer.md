# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T05:14:28.922556+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : HYPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.006 | entrée 7.000 | trend 8.250 | rang 7.722
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.722
2. ENA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.337
3. ADA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.077

## Accélération indépendante

- SYN-EUR — CONFIRMED_ACCELERATION — score 7.001/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- AAVE-EUR — ACTIVE_NOW — score mémoire 8.221/10 — sources ACCELERATION, V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 8.168/10 — sources V4 — WATCH_ONLY
- BEAM-EUR — ACTIVE_NOW — score mémoire 7.977/10 — sources V4 — WATCH_ONLY
- RAY-EUR — ACTIVE_NOW — score mémoire 7.975/10 — sources ACCELERATION, V4 — WATCH_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 7.971/10 — sources V4 — WATCH_ONLY
- ACH-EUR — ACTIVE_NOW — score mémoire 7.841/10 — sources V4 — WATCH_ONLY
- NPC-EUR — ACTIVE_NOW — score mémoire 7.835/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- POL-EUR — ACTIVE_NOW — score mémoire 7.745/10 — sources ACCELERATION, V4 — WATCH_ONLY
- HYPE-EUR — ACTIVE_NOW — score mémoire 7.722/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SSV-EUR — ACTIVE_NOW — score mémoire 7.715/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- G-EUR +62.99% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- F-EUR +34.56% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CPOOL-EUR +31.95% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- STRK-EUR +31.09% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +28.76% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- XTZ-EUR +27.65% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZAMA-EUR +20.46% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +19.90% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- ZIG-EUR +19.14% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MORPHO-EUR +18.99% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
