# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-16T06:03:05.653234+00:00
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

- AMP-EUR — CONFIRMED_ACCELERATION — score 7.254/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZRC-EUR — CONFIRMED_ACCELERATION — score 6.696/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BEAM-EUR — BUILDING_ACCELERATION — score 6.108/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RAD-EUR — BUILDING_ACCELERATION — score 4.917/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CNPY-EUR — BUILDING_ACCELERATION — score 4.806/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- HNT-EUR — MEMORY_24H — score mémoire 8.218/10 — sources ACCELERATION — MEMORY_ONLY
- ASTER-EUR — MEMORY_24H — score mémoire 7.937/10 — sources ACCELERATION — MEMORY_ONLY
- NES-EUR — MEMORY_DECAY_24_72H — score mémoire 7.882/10 — sources ACCELERATION — MEMORY_ONLY
- GLMR-EUR — MEMORY_24H — score mémoire 7.500/10 — sources ACCELERATION — MEMORY_ONLY
- AMP-EUR — ACTIVE_NOW — score mémoire 7.254/10 — sources ACCELERATION — WATCH_ONLY
- GNS-EUR — MEMORY_24H — score mémoire 7.099/10 — sources ACCELERATION — MEMORY_ONLY
- KITE-EUR — ACTIVE_NOW — score mémoire 7.094/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- CROSS-EUR — MEMORY_24H — score mémoire 6.926/10 — sources V4 — MEMORY_ONLY
- DODO-EUR — MEMORY_24H — score mémoire 6.888/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZRC-EUR — ACTIVE_NOW — score mémoire 6.696/10 — sources ACCELERATION — WATCH_ONLY

## Audit des plus fortes hausses

- RARE-EUR +63.23% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- WIN-EUR +20.91% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AXIS-EUR +16.12% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GLMR-EUR +13.29% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BIRB-EUR +12.79% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NES-EUR +10.68% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CSPR-EUR +7.99% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CPOOL-EUR +7.08% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- CROSS-EUR +6.69% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QNT-EUR +6.19% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
