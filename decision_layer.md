# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-15T13:06:44.207529+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : VTHO-EUR | action LATENT_ACCELERATOR | opportunité 8.237 | entrée 4.850 | trend 9.200 | rang 7.205
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : aucun candidat matériel

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.205

## Accélération indépendante

- XRP-EUR — BUILDING_ACCELERATION — score 6.342/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- LAPTOP-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 8.158/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ATOM-EUR — ACTIVE_NOW — score mémoire 8.079/10 — sources V4 — DETECTED_BUT_TOO_LATE
- LDO-EUR — ACTIVE_NOW — score mémoire 7.891/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.887/10 — sources V4 — WATCH_ONLY
- PEAQ-EUR — ACTIVE_NOW — score mémoire 7.756/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.708/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.682/10 — sources V4 — WATCH_ONLY
- PUMP-EUR — ACTIVE_NOW — score mémoire 7.652/10 — sources V4 — WATCH_ONLY
- SPX-EUR — ACTIVE_NOW — score mémoire 7.652/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ALIGN-EUR +38.93% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PUFFER-EUR +27.48% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +26.35% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ASTR-EUR +20.35% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +17.58% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- VTHO-EUR +14.80% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- INIT-EUR +13.37% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- CROSS-EUR +13.29% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LAPTOP-EUR +9.86% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- USELESS-EUR +8.96% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
