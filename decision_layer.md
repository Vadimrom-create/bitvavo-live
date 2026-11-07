# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-07T19:31:13.598141+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : INJ-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.408 | entrée 7.250 | trend 8.200 | rang 7.209
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. INJ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.209
2. BIRB-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.819
3. TRUST-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.776

## Accélération indépendante

- DGB-EUR — CONFIRMED_ACCELERATION — score 9.403/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LAPTOP-EUR — BUILDING_ACCELERATION — score 5.740/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- DGB-EUR — ACTIVE_NOW — score mémoire 9.403/10 — sources ACCELERATION — WATCH_ONLY
- HFT-EUR — MEMORY_DECAY_24_72H — score mémoire 9.368/10 — sources ACCELERATION — MEMORY_ONLY
- CARV-EUR — MEMORY_24H — score mémoire 9.061/10 — sources ACCELERATION — MEMORY_ONLY
- 2Z-EUR — MEMORY_24H — score mémoire 8.929/10 — sources ACCELERATION — MEMORY_ONLY
- BOB-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- GNS-EUR — MEMORY_DECAY_24_72H — score mémoire 8.053/10 — sources ACCELERATION — MEMORY_ONLY
- CT-EUR — MEMORY_24H — score mémoire 7.602/10 — sources ACCELERATION — MEMORY_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 7.209/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- NES-EUR — MEMORY_24H — score mémoire 7.125/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AXIS-EUR — MEMORY_24H — score mémoire 6.906/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- EPIC-EUR +41.51% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DEGEN-EUR +17.68% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MET-EUR +16.68% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ICNT-EUR +11.58% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NOS-EUR +10.40% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- ACT-EUR +9.96% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DGB-EUR +8.49% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- THE-EUR +7.37% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NES-EUR +6.41% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MAVIA-EUR +6.40% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
