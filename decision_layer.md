# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T03:32:27.075124+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : VTHO-EUR | action LATENT_ACCELERATOR | opportunité 7.905 | entrée 5.500 | trend 9.200 | rang 7.848
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : TAO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.083 | entrée 6.750 | trend 7.650 | rang 7.435
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.848
2. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.435

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- ICP-EUR — ACTIVE_NOW — score mémoire 8.496/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.315/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 8.123/10 — sources V4 — WATCH_ONLY
- LAPTOP-EUR — MEMORY_24H — score mémoire 8.013/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.940/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.934/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.903/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.848/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.839/10 — sources V4 — WATCH_ONLY
- KAVA-EUR — ACTIVE_NOW — score mémoire 7.775/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- REZ-EUR +26.56% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CPOOL-EUR +25.80% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FIL-EUR +21.88% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CVC-EUR +21.88% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZKJ-EUR +17.66% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- IQ-EUR +16.04% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- MTL-EUR +11.80% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LIGHTER-EUR +9.77% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NPC-EUR +8.33% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- BABY-EUR +6.59% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
