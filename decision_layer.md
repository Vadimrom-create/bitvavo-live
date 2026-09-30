# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-30T05:44:39.336888+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AVNT-EUR | action ACHETE_MAINTENANT | opportunité 9.235 | entrée 6.950 | trend 8.200 | rang 8.194
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ALICE-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.121 | entrée 6.150 | trend 8.700 | rang 7.655
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : COMP-EUR | action LATENT_ACCELERATOR | opportunité 7.908 | entrée 5.300 | trend 9.200 | rang 7.767
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : ICP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.788 | entrée 6.650 | trend 9.200 | rang 8.283
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. AVNT-EUR — ACHETE_MAINTENANT — rank 8.194 — opportunité 9.235 — entrée 6.950 — trend 8.200
2. ADA-EUR — ACHETE_MAINTENANT — rank 7.625 — opportunité 8.983 — entrée 7.700 — trend 7.100

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ICP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.283
2. AVNT-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.194
3. SEI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.960

## Accélération indépendante

- MOVR-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- NIL-EUR — CONFIRMED_ACCELERATION — score 8.340/10 — DETECTED_BUT_TOO_LATE
- GNS-EUR — CONFIRMED_ACCELERATION — score 7.896/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GTC-EUR — CONFIRMED_ACCELERATION — score 7.802/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TAI-EUR — CONFIRMED_ACCELERATION — score 7.481/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SOMI-EUR — CONFIRMED_ACCELERATION — score 7.399/10 — DETECTED_BUT_TOO_LATE
- PHA-EUR — CONFIRMED_ACCELERATION — score 7.177/10 — DETECTED_BUT_TOO_LATE
- SCR-EUR — CONFIRMED_ACCELERATION — score 7.045/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NPC-EUR — BUILDING_ACCELERATION — score 6.405/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FUEL-EUR — BUILDING_ACCELERATION — score 6.268/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ICP-EUR — ACTIVE_NOW — score mémoire 8.283/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- SWELL-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- QUID-EUR — MEMORY_24H — score mémoire 8.702/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MOVR-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- NIL-EUR — ACTIVE_NOW — score mémoire 8.340/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- AGI-EUR — MEMORY_24H — score mémoire 8.300/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AVNT-EUR — ACTIVE_NOW — score mémoire 8.194/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SOLV-EUR — MEMORY_24H — score mémoire 8.017/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SEI-EUR — ACTIVE_NOW — score mémoire 7.960/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LTC-EUR — ACTIVE_NOW — score mémoire 7.943/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SOON-EUR +47.06% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MOVR-EUR +47.05% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZBCN-EUR +28.75% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MEW-EUR +22.14% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZRO-EUR +21.33% — DETECTED_EARLY — couche NONE — action NONE
- PUMP-EUR +18.18% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PHA-EUR +17.53% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- INIT-EUR +17.03% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- QNT-EUR +15.65% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FUEL-EUR +14.58% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE

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
