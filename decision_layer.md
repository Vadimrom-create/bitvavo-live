# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-02T18:52:51.266728+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : aucun candidat matériel

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
Aucun candidat ne remplit actuellement un bucket décisionnel.

## Accélération indépendante

- MAVIA-EUR — BUILDING_ACCELERATION — score 5.646/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PTB-EUR — BUILDING_ACCELERATION — score 5.311/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CSPR-EUR — BUILDING_ACCELERATION — score 5.270/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ACU-EUR — MEMORY_24H — score mémoire 9.208/10 — sources ACCELERATION — MEMORY_ONLY
- RUNE-EUR — MEMORY_24H — score mémoire 8.445/10 — sources ACCELERATION — MEMORY_ONLY
- PEPE-EUR — MEMORY_24H — score mémoire 6.931/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SOLV-EUR — MEMORY_24H — score mémoire 6.894/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WIN-EUR — MEMORY_24H — score mémoire 6.783/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PARTI-EUR — MEMORY_24H — score mémoire 6.415/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- INIT-EUR — MEMORY_24H — score mémoire 6.318/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- HAEDAL-EUR — MEMORY_24H — score mémoire 6.255/10 — sources ACCELERATION, DECISION_LAYER — MEMORY_ONLY
- G-EUR — MEMORY_DECAY_24_72H — score mémoire 6.110/10 — sources ACCELERATION — MEMORY_ONLY
- ADX-EUR — MEMORY_DECAY_24_72H — score mémoire 5.653/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- XMN-EUR +36.19% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- U-EUR +17.46% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- HOT-EUR +13.35% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CAT-EUR +9.30% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FUEL-EUR +9.25% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- HAEDAL-EUR +9.20% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CSPR-EUR +7.86% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- IMU-EUR +5.32% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NES-EUR +5.18% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- LAPTOP-EUR +4.82% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
