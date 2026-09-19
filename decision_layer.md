# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T00:11:48.705932+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : TAO-EUR | action ACHETE_MAINTENANT | opportunité 8.262 | entrée 7.600 | trend 5.150 | rang 6.661
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : HYPE-EUR | action LATENT_ACCELERATOR | opportunité 7.501 | entrée 4.500 | trend 8.400 | rang 7.169
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : PEPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.904 | entrée 6.250 | trend 8.950 | rang 7.836
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. PEPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.836
2. LTC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.570
3. HYPE-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.169

## Accélération indépendante

- TAO-EUR — BUILDING_ACCELERATION — score 5.368/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- GRT-EUR — ACTIVE_NOW — score mémoire 8.315/10 — sources V4 — WATCH_ONLY
- SYN-EUR — MEMORY_24H — score mémoire 8.311/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- VTHO-EUR — MEMORY_24H — score mémoire 8.268/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.096/10 — sources ACCELERATION, V4 — WATCH_ONLY
- ZRX-EUR — ACTIVE_NOW — score mémoire 7.968/10 — sources V4 — WATCH_ONLY
- YB-EUR — MEMORY_24H — score mémoire 7.953/10 — sources V4 — MEMORY_ONLY
- GALA-EUR — ACTIVE_NOW — score mémoire 7.926/10 — sources V4 — WATCH_ONLY
- ROSE-EUR — ACTIVE_NOW — score mémoire 7.921/10 — sources V4 — WATCH_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 7.879/10 — sources V4 — WATCH_ONLY
- FET-EUR — ACTIVE_NOW — score mémoire 7.857/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- F-EUR +58.31% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +54.39% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +49.33% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARB-EUR +25.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- APT-EUR +23.66% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- C-EUR +23.29% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZIG-EUR +21.52% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QKC-EUR +20.86% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- OP-EUR +19.76% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZAMA-EUR +19.60% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
