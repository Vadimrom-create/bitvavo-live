# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-13T20:01:13.944773+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : ZIL-EUR | action LATENT_ACCELERATOR | opportunité 7.770 | entrée 5.300 | trend 8.450 | rang 6.539
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.983 | entrée 6.000 | trend 9.200 | rang 6.942
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.942
2. ZIL-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 6.539

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- VET-EUR — ACTIVE_NOW — score mémoire 8.053/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ATOM-EUR — ACTIVE_NOW — score mémoire 7.822/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.755/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.672/10 — sources V4 — WATCH_ONLY
- KSM-EUR — ACTIVE_NOW — score mémoire 7.647/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.607/10 — sources V4 — WATCH_ONLY
- NPC-EUR — ACTIVE_NOW — score mémoire 7.595/10 — sources ACCELERATION, V4 — WATCH_ONLY
- QKC-EUR — MEMORY_24H — score mémoire 7.588/10 — sources V4 — MEMORY_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 7.587/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- CAKE-EUR — ACTIVE_NOW — score mémoire 7.547/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- LSK-EUR +280.57% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- CVC-EUR +59.76% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- REZ-EUR +24.74% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FIL-EUR +22.69% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VTHO-EUR +19.99% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZIL-EUR +18.60% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARK-EUR +17.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +14.00% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOLV-EUR +13.49% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- POWR-EUR +12.88% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
