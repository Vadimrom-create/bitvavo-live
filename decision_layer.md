# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-15T14:23:51.917089+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : USELESS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.401 | entrée 6.300 | trend 8.100 | rang 7.037
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.037
2. NPC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.002
3. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.928

## Accélération indépendante

- LSK-EUR — CONFIRMED_ACCELERATION — score 7.664/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- LAPTOP-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- UNI-EUR — MEMORY_24H — score mémoire 7.931/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.848/10 — sources V4 — WATCH_ONLY
- TIA-EUR — MEMORY_24H — score mémoire 7.702/10 — sources V4 — MEMORY_ONLY
- LSK-EUR — ACTIVE_NOW — score mémoire 7.664/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.638/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.581/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.575/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.567/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- WIF-EUR — MEMORY_24H — score mémoire 7.528/10 — sources V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- ALIGN-EUR +38.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +31.91% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PUFFER-EUR +24.93% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +19.57% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- GLMR-EUR +17.32% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ASTR-EUR +16.10% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +14.75% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- VTHO-EUR +13.26% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- LAPTOP-EUR +8.21% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- POWR-EUR +6.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
