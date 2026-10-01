# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-01T14:56:12.448162+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AAVE-EUR | action ACHETE_MAINTENANT | opportunité 8.249 | entrée 7.000 | trend 8.900 | rang 7.991
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : LRC-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.520 | entrée 6.500 | trend 8.400 | rang 7.443
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : KSM-EUR | action LATENT_ACCELERATOR | opportunité 7.530 | entrée 4.750 | trend 8.900 | rang 7.478
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : PROM-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.133 | entrée 6.450 | trend 8.950 | rang 7.938
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. AAVE-EUR — ACHETE_MAINTENANT — rank 7.991 — opportunité 8.249 — entrée 7.000 — trend 8.900
2. SYRUP-EUR — ACHETE_MAINTENANT — rank 7.388 — opportunité 8.839 — entrée 6.950 — trend 6.800

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. AAVE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.991
2. PROM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.938
3. WLD-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.916

## Accélération indépendante

- ALICE-EUR — CONFIRMED_ACCELERATION — score 9.027/10 — DETECTED_BUT_TOO_LATE
- GLMR-EUR — CONFIRMED_ACCELERATION — score 7.866/10 — DETECTED_BUT_TOO_LATE
- CHILLGUY-EUR — BUILDING_ACCELERATION — score 6.288/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PONKE-EUR — BUILDING_ACCELERATION — score 5.876/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- REQ-EUR — BUILDING_ACCELERATION — score 5.825/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- CPOOL-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XYO-EUR — MEMORY_24H — score mémoire 9.473/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ALICE-EUR — ACTIVE_NOW — score mémoire 9.027/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- CT-EUR — MEMORY_24H — score mémoire 8.691/10 — sources ACCELERATION — MEMORY_ONLY
- ARPA-EUR — MEMORY_24H — score mémoire 8.595/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 8.568/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TAI-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ACE-EUR — MEMORY_24H — score mémoire 8.405/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- OSMO-EUR — MEMORY_24H — score mémoire 8.342/10 — sources ACCELERATION — MEMORY_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 7.991/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SWEAT-EUR +119.74% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- MOVR-EUR +60.07% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CAP-EUR +30.23% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- CT-EUR +29.41% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ALICE-EUR +20.81% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- SYN-EUR +16.18% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MON-EUR +15.76% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NOS-EUR +15.35% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HEI-EUR +13.06% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- STX-EUR +13.06% — DETECTED_EARLY — couche NONE — action INTERPRETATION

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
