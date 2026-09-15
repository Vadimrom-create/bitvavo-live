# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-15T08:25:54.323451+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.251 | entrée 7.100 | trend 9.200 | rang 8.028
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.028
2. NPC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.111
3. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.035

## Accélération indépendante

- PUNDIX-EUR — BUILDING_ACCELERATION — score 5.907/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- CAP-EUR — MEMORY_24H — score mémoire 9.037/10 — sources ACCELERATION — MEMORY_ONLY
- LAPTOP-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.028/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.803/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.690/10 — sources V4 — WATCH_ONLY
- CHIP-EUR — MEMORY_24H — score mémoire 7.626/10 — sources V4 — MEMORY_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.624/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.582/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.532/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- WIF-EUR — MEMORY_24H — score mémoire 7.528/10 — sources V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- PUFFER-EUR +25.90% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CAP-EUR +25.71% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +25.07% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ASTR-EUR +16.45% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +12.72% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ACX-EUR +11.82% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ACE-EUR +11.57% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- LRC-EUR +9.11% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- AXL-EUR +8.24% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LAPTOP-EUR +7.43% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
