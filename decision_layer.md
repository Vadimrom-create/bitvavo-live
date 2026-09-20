# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T05:55:55.847582+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : UNI-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.668 | entrée 6.950 | trend 7.650 | rang 7.511
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. UNI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.511
2. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.232
3. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.981

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- C-EUR — MEMORY_24H — score mémoire 8.647/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- COW-EUR — ACTIVE_NOW — score mémoire 8.367/10 — sources V4 — WATCH_ONLY
- NPC-EUR — MEMORY_24H — score mémoire 7.903/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- VVV-EUR — ACTIVE_NOW — score mémoire 7.866/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- COTI-EUR — ACTIVE_NOW — score mémoire 7.860/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 7.832/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- DOT-EUR — MEMORY_24H — score mémoire 7.831/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.830/10 — sources V4 — WATCH_ONLY
- ETC-EUR — MEMORY_24H — score mémoire 7.770/10 — sources V4 — MEMORY_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.734/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CELR-EUR +110.92% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +81.00% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZAMA-EUR +31.68% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CTSI-EUR +29.00% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SKL-EUR +25.39% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIL-EUR +23.10% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- C-EUR +21.33% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- STX-EUR +17.91% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ONG-EUR +14.78% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- RLC-EUR +13.69% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
