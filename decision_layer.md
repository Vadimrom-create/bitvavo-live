# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-09T11:22:58.297922+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : MEGA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.434 | entrée 6.650 | trend 8.750 | rang 7.340
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : aucun candidat matériel

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. MEGA-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.340

## Accélération indépendante

- ZIL-EUR — CONFIRMED_ACCELERATION — score 9.775/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- USELESS-EUR — CONFIRMED_ACCELERATION — score 8.089/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- QUID-EUR — CONFIRMED_ACCELERATION — score 7.572/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CHILLGUY-EUR — CONFIRMED_ACCELERATION — score 7.541/10 — DETECTED_BUT_TOO_LATE
- TRUST-EUR — CONFIRMED_ACCELERATION — score 7.087/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SCR-EUR — CONFIRMED_ACCELERATION — score 6.796/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MEGA-EUR — CONFIRMED_ACCELERATION — score 6.689/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- INJ-EUR — BUILDING_ACCELERATION — score 6.406/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CHIP-EUR — BUILDING_ACCELERATION — score 6.360/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CVX-EUR — BUILDING_ACCELERATION — score 5.861/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ZIL-EUR — ACTIVE_NOW — score mémoire 9.775/10 — sources ACCELERATION — WATCH_ONLY
- WIN-EUR — MEMORY_24H — score mémoire 9.248/10 — sources ACCELERATION — MEMORY_ONLY
- EPIC-EUR — MEMORY_24H — score mémoire 8.694/10 — sources ACCELERATION — MEMORY_ONLY
- USELESS-EUR — ACTIVE_NOW — score mémoire 8.089/10 — sources ACCELERATION — WATCH_ONLY
- QUID-EUR — ACTIVE_NOW — score mémoire 7.572/10 — sources ACCELERATION — WATCH_ONLY
- CHILLGUY-EUR — ACTIVE_NOW — score mémoire 7.541/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- OSMO-EUR — MEMORY_24H — score mémoire 7.500/10 — sources ACCELERATION — MEMORY_ONLY
- XMN-EUR — MEMORY_DECAY_24_72H — score mémoire 7.382/10 — sources ACCELERATION — MEMORY_ONLY
- MEGA-EUR — ACTIVE_NOW — score mémoire 7.340/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- TRUST-EUR — ACTIVE_NOW — score mémoire 7.087/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- GNS-EUR +51.36% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- RSR-EUR +7.90% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NES-EUR +7.66% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- MERL-EUR +7.54% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZIL-EUR +6.99% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- O-EUR +5.93% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARB-EUR +5.03% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- BIO-EUR +4.66% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- BIRB-EUR +4.62% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- DODO-EUR +4.56% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Gestion des positions détenues

Policy : STAGED_10_20_RUNNER_V1
- +10% : prise partielle 35%.
- +20% : seconde prise 35%.
- Runner conservé : 30%.
- Revue coût d'opportunité après 72 h ; sortie seulement avant la première partielle, proche/sous le PRU et avec momentum 15m affaibli.
- Pas de stop serré mécaniquement après une petite hausse ; le stop reste lié à l'invalidation structurelle.

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
