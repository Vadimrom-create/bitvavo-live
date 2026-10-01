# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-01T19:58:50.154637+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : LINK-EUR | action ACHETE_MAINTENANT | opportunité 9.077 | entrée 7.900 | trend 8.000 | rang 8.230
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : GALA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.616 | entrée 6.700 | trend 8.450 | rang 7.571
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : KSM-EUR | action LATENT_ACCELERATOR | opportunité 8.324 | entrée 4.300 | trend 9.200 | rang 7.897
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : PUMP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.964 | entrée 6.800 | trend 8.500 | rang 8.052
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. LINK-EUR — ACHETE_MAINTENANT — rank 8.230 — opportunité 9.077 — entrée 7.900 — trend 8.000
2. AAVE-EUR — ACHETE_MAINTENANT — rank 8.178 — opportunité 8.567 — entrée 7.200 — trend 8.900
3. SUI-EUR — ACHETE_MAINTENANT — rank 7.806 — opportunité 8.095 — entrée 7.200 — trend 8.400
4. LTC-EUR — ACHETE_MAINTENANT — rank 7.048 — opportunité 8.696 — entrée 7.850 — trend 5.850

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. LINK-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.230
2. AAVE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.178
3. PUMP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.052

## Accélération indépendante

- SUPER-EUR — CONFIRMED_ACCELERATION — score 8.570/10 — DETECTED_BUT_TOO_LATE
- WLD-EUR — BUILDING_ACCELERATION — score 5.669/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SQD-EUR — BUILDING_ACCELERATION — score 5.644/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PUMP-EUR — BUILDING_ACCELERATION — score 5.399/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XMN-EUR — BUILDING_ACCELERATION — score 5.226/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- CPOOL-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 8.692/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CT-EUR — MEMORY_24H — score mémoire 8.691/10 — sources ACCELERATION — MEMORY_ONLY
- SUPER-EUR — ACTIVE_NOW — score mémoire 8.570/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- CHILLGUY-EUR — MEMORY_24H — score mémoire 8.548/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- OSMO-EUR — MEMORY_24H — score mémoire 8.342/10 — sources ACCELERATION — MEMORY_ONLY
- LINK-EUR — ACTIVE_NOW — score mémoire 8.230/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.178/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ALICE-EUR — MEMORY_24H — score mémoire 8.163/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AGI-EUR — MEMORY_24H — score mémoire 8.119/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- SWEAT-EUR +143.18% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- MOVR-EUR +70.02% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ALICE-EUR +35.81% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GTC-EUR +29.30% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CAP-EUR +26.12% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- MEGA-EUR +24.48% — DETECTED_EARLY — couche NONE — action NONE
- MON-EUR +21.81% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- VELO-EUR +20.19% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SYN-EUR +19.49% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MOVE-EUR +19.31% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
