# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-06T22:18:29.291521+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : CAP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.739 | entrée 5.800 | trend 7.850 | rang 6.588
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. CAP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.588
2. ELSA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.495
3. BIRB-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.425

## Accélération indépendante

- AXIS-EUR — CONFIRMED_ACCELERATION — score 6.906/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PROMPT-EUR — BUILDING_ACCELERATION — score 6.328/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZBCN-EUR — BUILDING_ACCELERATION — score 6.171/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WIN-EUR — BUILDING_ACCELERATION — score 5.132/10 — DETECTED_BUT_TOO_LATE
- ALIGN-EUR — BUILDING_ACCELERATION — score 4.954/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CSPR-EUR — BUILDING_ACCELERATION — score 4.844/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CHIP-EUR — BUILDING_ACCELERATION — score 4.837/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- HFT-EUR — MEMORY_24H — score mémoire 9.777/10 — sources ACCELERATION — MEMORY_ONLY
- TRIA-EUR — MEMORY_24H — score mémoire 9.163/10 — sources ACCELERATION — MEMORY_ONLY
- PTB-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- WHUF-EUR — MEMORY_24H — score mémoire 8.439/10 — sources ACCELERATION — MEMORY_ONLY
- GNS-EUR — MEMORY_24H — score mémoire 8.404/10 — sources ACCELERATION — MEMORY_ONLY
- LAPTOP-EUR — MEMORY_24H — score mémoire 7.098/10 — sources ACCELERATION — MEMORY_ONLY
- AXIS-EUR — ACTIVE_NOW — score mémoire 6.906/10 — sources ACCELERATION — WATCH_ONLY
- QKC-EUR — MEMORY_24H — score mémoire 6.775/10 — sources ACCELERATION — MEMORY_ONLY
- THE-EUR — MEMORY_24H — score mémoire 6.735/10 — sources ACCELERATION — MEMORY_ONLY
- INX-EUR — MEMORY_24H — score mémoire 6.729/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- ICNT-EUR +40.42% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CYBER-EUR +27.56% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GROVE-EUR +20.97% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ACT-EUR +17.48% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TRIA-EUR +13.90% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- XTZ-EUR +12.42% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- FLOCK-EUR +12.30% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CELR-EUR +12.28% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- SAFE-EUR +11.24% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- BIRB-EUR +10.70% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
