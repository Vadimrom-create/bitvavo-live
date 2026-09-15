# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-15T08:01:28.134489+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.790 | entrée 5.900 | trend 9.200 | rang 7.538
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.538
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.056
3. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.017

## Accélération indépendante

- LAPTOP-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CAP-EUR — MEMORY_24H — score mémoire 9.037/10 — sources ACCELERATION — MEMORY_ONLY
- LAPTOP-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- DOT-EUR — ACTIVE_NOW — score mémoire 7.961/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- LDO-EUR — ACTIVE_NOW — score mémoire 7.923/10 — sources V4 — WATCH_ONLY
- BNB-EUR — ACTIVE_NOW — score mémoire 7.893/10 — sources V4 — WATCH_ONLY
- ATOM-EUR — ACTIVE_NOW — score mémoire 7.762/10 — sources V4 — DETECTED_BUT_TOO_LATE
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.687/10 — sources V4 — WATCH_ONLY
- AKT-EUR — ACTIVE_NOW — score mémoire 7.644/10 — sources V4 — WATCH_ONLY
- PEAQ-EUR — MEMORY_24H — score mémoire 7.633/10 — sources V4 — MEMORY_ONLY
- CHIP-EUR — MEMORY_24H — score mémoire 7.626/10 — sources V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- CAP-EUR +27.44% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +24.89% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PUFFER-EUR +19.82% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LAPTOP-EUR +18.69% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ASTR-EUR +13.37% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ACE-EUR +12.38% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- ACX-EUR +11.82% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CROSS-EUR +8.47% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +7.90% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- ZRC-EUR +7.48% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
