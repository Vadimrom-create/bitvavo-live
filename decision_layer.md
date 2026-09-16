# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-16T13:58:44.893793+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : USELESS-EUR | action LATENT_ACCELERATOR | opportunité 7.446 | entrée 5.700 | trend 8.100 | rang 6.517
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : NEAR-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.732 | entrée 7.450 | trend 8.100 | rang 7.435
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.435
2. NPC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.273
3. USELESS-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 6.517

## Accélération indépendante

- RAY-EUR — BUILDING_ACCELERATION — score 5.476/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- WLD-EUR — ACTIVE_NOW — score mémoire 8.154/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 8.075/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- LDO-EUR — ACTIVE_NOW — score mémoire 8.046/10 — sources V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.931/10 — sources V4 — WATCH_ONLY
- ZORA-EUR — ACTIVE_NOW — score mémoire 7.889/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — MEMORY_24H — score mémoire 7.864/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ATOM-EUR — ACTIVE_NOW — score mémoire 7.860/10 — sources V4 — DETECTED_BUT_TOO_LATE
- ICP-EUR — ACTIVE_NOW — score mémoire 7.818/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.806/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.713/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SYN-EUR +116.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LSK-EUR +52.49% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FOLD-EUR +20.28% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- HEI-EUR +19.34% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ARB-EUR +18.20% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- USELESS-EUR +15.93% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CNPY-EUR +10.49% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- IOST-EUR +10.05% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TAI-EUR +9.90% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +8.31% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
