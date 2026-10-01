# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-01T00:34:19.224858+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : DIA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.206 | entrée 5.950 | trend 8.750 | rang 7.815
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : TRB-EUR | action LATENT_ACCELERATOR | opportunité 7.681 | entrée 5.500 | trend 8.850 | rang 7.619
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : W-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.803 | entrée 7.200 | trend 8.150 | rang 8.019
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. W-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.019
2. KSM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.007
3. ICP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.955

## Accélération indépendante

- ARK-EUR — CONFIRMED_ACCELERATION — score 7.500/10 — DETECTED_BUT_TOO_LATE
- TRAC-EUR — BUILDING_ACCELERATION — score 5.873/10 — DETECTED_BUT_TOO_LATE
- MON-EUR — BUILDING_ACCELERATION — score 5.829/10 — DETECTED_BUT_TOO_LATE
- DRV-EUR — BUILDING_ACCELERATION — score 5.752/10 — DETECTED_BUT_TOO_LATE
- ESP-EUR — BUILDING_ACCELERATION — score 5.670/10 — DETECTED_BUT_TOO_LATE
- HAEDAL-EUR — BUILDING_ACCELERATION — score 5.033/10 — DETECTED_BUT_TOO_LATE
- CELO-EUR — BUILDING_ACCELERATION — score 4.819/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- LMWR-EUR — MEMORY_24H — score mémoire 9.685/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CTR-EUR — MEMORY_24H — score mémoire 8.902/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ARPA-EUR — MEMORY_24H — score mémoire 8.595/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- HNT-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MOVR-EUR — MEMORY_24H — score mémoire 8.404/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 8.400/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GWEI-EUR — MEMORY_24H — score mémoire 8.214/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- W-EUR — ACTIVE_NOW — score mémoire 8.019/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KSM-EUR — ACTIVE_NOW — score mémoire 8.007/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.955/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- MOVR-EUR +87.70% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CT-EUR +49.72% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GLMR-EUR +26.27% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- MON-EUR +21.60% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- STX-EUR +18.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOON-EUR +18.36% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TRAC-EUR +17.53% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CAP-EUR +15.22% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- NOM-EUR +11.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SOMI-EUR +10.83% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
