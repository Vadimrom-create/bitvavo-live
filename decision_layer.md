# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-01T20:43:09.200525+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AAVE-EUR | action ACHETE_MAINTENANT | opportunité 9.514 | entrée 7.450 | trend 9.200 | rang 8.724
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : C-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.607 | entrée 6.450 | trend 8.700 | rang 7.635
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : DIA-EUR | action LATENT_ACCELERATOR | opportunité 8.352 | entrée 4.550 | trend 9.000 | rang 7.809
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : GALA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.074 | entrée 6.500 | trend 8.450 | rang 8.196
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. AAVE-EUR — ACHETE_MAINTENANT — rank 8.724 — opportunité 9.514 — entrée 7.450 — trend 9.200
2. WLD-EUR — ACHETE_MAINTENANT — rank 8.491 — opportunité 9.399 — entrée 7.800 — trend 8.650
3. PUMP-EUR — ACHETE_MAINTENANT — rank 8.292 — opportunité 9.271 — entrée 7.500 — trend 8.500
4. BABY-EUR — ACHETE_MAINTENANT — rank 8.188 — opportunité 9.174 — entrée 7.000 — trend 8.200
5. AVAX-EUR — ACHETE_MAINTENANT — rank 8.052 — opportunité 8.352 — entrée 7.400 — trend 8.700
6. SUI-EUR — ACHETE_MAINTENANT — rank 7.765 — opportunité 8.129 — entrée 7.350 — trend 8.400
7. LTC-EUR — ACHETE_MAINTENANT — rank 7.045 — opportunité 8.360 — entrée 7.500 — trend 6.100

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. AAVE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.724
2. WLD-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.491
3. PUMP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.292

## Accélération indépendante

- GTC-EUR — CONFIRMED_ACCELERATION — score 8.875/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CPOOL-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GTC-EUR — ACTIVE_NOW — score mémoire 8.875/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.724/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CT-EUR — MEMORY_24H — score mémoire 8.691/10 — sources ACCELERATION — MEMORY_ONLY
- CHILLGUY-EUR — MEMORY_24H — score mémoire 8.548/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 8.491/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- OSMO-EUR — MEMORY_24H — score mémoire 8.342/10 — sources ACCELERATION — MEMORY_ONLY
- PUMP-EUR — ACTIVE_NOW — score mémoire 8.292/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- GALA-EUR — ACTIVE_NOW — score mémoire 8.196/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- BABY-EUR — ACTIVE_NOW — score mémoire 8.188/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SWEAT-EUR +155.12% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- MOVR-EUR +60.03% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ALICE-EUR +40.84% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GTC-EUR +35.97% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CAP-EUR +23.60% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- MEGA-EUR +23.40% — DETECTED_EARLY — couche NONE — action NONE
- NOS-EUR +20.00% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CT-EUR +18.78% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MOVE-EUR +18.40% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NOM-EUR +18.16% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
