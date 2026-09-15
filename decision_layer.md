# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-15T08:47:50.878551+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.726 | entrée 6.350 | trend 8.650 | rang 7.670
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.670
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.159
3. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.034

## Accélération indépendante

- CAP-EUR — CONFIRMED_ACCELERATION — score 8.000/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- LAPTOP-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CAP-EUR — ACTIVE_NOW — score mémoire 8.000/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- ATOM-EUR — ACTIVE_NOW — score mémoire 7.846/10 — sources V4 — DETECTED_BUT_TOO_LATE
- LDO-EUR — ACTIVE_NOW — score mémoire 7.767/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.753/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.713/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.670/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.635/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.635/10 — sources V4 — WATCH_ONLY
- CHIP-EUR — MEMORY_24H — score mémoire 7.626/10 — sources V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- CAP-EUR +33.62% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PUFFER-EUR +25.83% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +23.05% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ASTR-EUR +18.22% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +13.90% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ACE-EUR +13.44% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- ACX-EUR +11.82% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- AXL-EUR +9.82% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +8.77% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- COTI-EUR +7.26% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
