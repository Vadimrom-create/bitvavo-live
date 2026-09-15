# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-15T06:21:25.143751+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.896 | entrée 5.750 | trend 9.200 | rang 7.324
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.324
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.320
3. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.214

## Accélération indépendante

- LSK-EUR — BUILDING_ACCELERATION — score 5.836/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CAP-EUR — MEMORY_24H — score mémoire 9.037/10 — sources ACCELERATION — MEMORY_ONLY
- CNPY-EUR — MEMORY_24H — score mémoire 8.734/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.073/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.880/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 7.837/10 — sources V4 — WATCH_ONLY
- LIGHTER-EUR — ACTIVE_NOW — score mémoire 7.783/10 — sources V4 — WATCH_ONLY
- ZORA-EUR — ACTIVE_NOW — score mémoire 7.747/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.742/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.686/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.669/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- PUFFER-EUR +38.37% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CAP-EUR +31.97% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +21.27% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- AXL-EUR +16.74% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- CTR-EUR +15.42% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ACX-EUR +11.51% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ASTR-EUR +10.76% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- INIT-EUR +7.60% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- MIRA-EUR +6.61% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- NOT-EUR +6.50% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
