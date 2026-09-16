# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-16T22:22:12.316024+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : USELESS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.788 | entrée 7.250 | trend 8.100 | rang 7.164
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.164

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- SIGN-EUR — ACTIVE_NOW — score mémoire 8.035/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.028/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.938/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.881/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.871/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AKT-EUR — MEMORY_24H — score mémoire 7.849/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.720/10 — sources V4 — WATCH_ONLY
- FORM-EUR — ACTIVE_NOW — score mémoire 7.714/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.708/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- LINEA-EUR — MEMORY_24H — score mémoire 7.666/10 — sources V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- SYN-EUR +82.04% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- HNT-EUR +38.87% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LSK-EUR +37.48% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HEI-EUR +29.92% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FOLD-EUR +23.01% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- IOST-EUR +15.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DGB-EUR +14.81% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- AGI-EUR +13.86% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- RAY-EUR +13.85% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +12.23% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
