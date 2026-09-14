# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T17:29:48.509957+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.904 | entrée 5.750 | trend 9.200 | rang 7.815
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.815
2. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.410
3. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.896

## Accélération indépendante

- USELESS-EUR — CONFIRMED_ACCELERATION — score 7.250/10 — DETECTED_BUT_TOO_LATE
- NEAR-EUR — BUILDING_ACCELERATION — score 5.998/10 — DETECTED_BUT_TOO_LATE
- CNPY-EUR — BUILDING_ACCELERATION — score 5.349/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- VET-EUR — ACTIVE_NOW — score mémoire 8.457/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.912/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.900/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.895/10 — sources V4 — WATCH_ONLY
- XPL-EUR — ACTIVE_NOW — score mémoire 7.835/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.815/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.779/10 — sources V4 — WATCH_ONLY
- IOST-EUR — ACTIVE_NOW — score mémoire 7.761/10 — sources V4 — DETECTED_BUT_TOO_LATE
- KAS-EUR — ACTIVE_NOW — score mémoire 7.744/10 — sources V4 — WATCH_ONLY
- SPX-EUR — ACTIVE_NOW — score mémoire 7.688/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CNPY-EUR +36.75% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CPOOL-EUR +34.01% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CAP-EUR +23.12% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARK-EUR +18.98% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- QKC-EUR +15.16% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- MTL-EUR +15.14% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- T-EUR +12.18% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SENT-EUR +11.96% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- ZRC-EUR +11.30% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NPC-EUR +10.74% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
