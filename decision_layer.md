# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-05T07:09:12.173768+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : STX-EUR | action ACHETE_MAINTENANT | opportunité 7.190 | entrée 6.900 | trend 8.300 | rang 7.147
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : C-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.604 | entrée 6.150 | trend 8.950 | rang 7.480
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : DEEP-EUR | action LATENT_ACCELERATOR | opportunité 7.791 | entrée 5.350 | trend 8.950 | rang 7.443
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AAVE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.659 | entrée 7.850 | trend 8.700 | rang 7.637
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. STX-EUR — ACHETE_MAINTENANT — rank 7.147 — opportunité 7.190 — entrée 6.900 — trend 8.300

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. AAVE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.637
2. SKY-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.633
3. BAT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.488

## Accélération indépendante

- ENA-EUR — CONFIRMED_ACCELERATION — score 7.316/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SWEAT-EUR — CONFIRMED_ACCELERATION — score 6.999/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRAC-EUR — CONFIRMED_ACCELERATION — score 6.957/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MASK-EUR — CONFIRMED_ACCELERATION — score 6.664/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GTC-EUR — CONFIRMED_ACCELERATION — score 6.649/10 — DETECTED_BUT_TOO_LATE
- MET-EUR — BUILDING_ACCELERATION — score 5.770/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WIN-EUR — BUILDING_ACCELERATION — score 5.332/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ARB-EUR — BUILDING_ACCELERATION — score 5.217/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MEGA-EUR — BUILDING_ACCELERATION — score 5.057/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SIGN-EUR — BUILDING_ACCELERATION — score 5.006/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- SWELL-EUR — MEMORY_24H — score mémoire 9.171/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FIDA-EUR — MEMORY_24H — score mémoire 9.160/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- HAEDAL-EUR — MEMORY_24H — score mémoire 9.157/10 — sources ACCELERATION — MEMORY_ONLY
- HNT-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- NIL-EUR — MEMORY_24H — score mémoire 8.392/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PORTAL-EUR — MEMORY_24H — score mémoire 8.374/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZKP-EUR — MEMORY_24H — score mémoire 8.310/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- W-EUR — MEMORY_24H — score mémoire 8.059/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MAV-EUR — MEMORY_24H — score mémoire 7.946/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SYRUP-EUR — MEMORY_24H — score mémoire 7.682/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- GTC-EUR +69.90% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NIL-EUR +19.91% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CARV-EUR +15.85% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FET-EUR +14.38% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SCR-EUR +13.75% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BEAM-EUR +13.35% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- HNT-EUR +12.12% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NOS-EUR +12.02% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ADA-EUR +11.03% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VIRTUAL-EUR +10.21% — DETECTED_EARLY — couche NONE — action INTERPRETATION

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
