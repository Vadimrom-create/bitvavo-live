# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-28T20:26:17.536143+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : PEPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.918 | entrée 7.550 | trend 8.800 | rang 7.105
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. PEPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.105
2. REZ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.815
3. ELSA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.792

## Accélération indépendante

- CSPR-EUR — CONFIRMED_ACCELERATION — score 7.185/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZBCN-EUR — BUILDING_ACCELERATION — score 6.243/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LAPTOP-EUR — BUILDING_ACCELERATION — score 5.507/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BEAM-EUR — BUILDING_ACCELERATION — score 4.981/10 — DETECTED_BUT_TOO_LATE
- PIXEL-EUR — BUILDING_ACCELERATION — score 4.769/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ZEUS-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION — MEMORY_ONLY
- AGI-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION — MEMORY_ONLY
- BLUR-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- ICNT-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- CELO-EUR — MEMORY_24H — score mémoire 7.853/10 — sources ACCELERATION — MEMORY_ONLY
- MEGA-EUR — ACTIVE_NOW — score mémoire 7.465/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CSPR-EUR — ACTIVE_NOW — score mémoire 7.185/10 — sources ACCELERATION — WATCH_ONLY
- BABY-EUR — ACTIVE_NOW — score mémoire 7.170/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PEPE-EUR — ACTIVE_NOW — score mémoire 7.105/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- PARTI-EUR — ACTIVE_NOW — score mémoire 6.987/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- XMN-EUR +117.69% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZEUS-EUR +31.99% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- XAN-EUR +23.35% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BLUR-EUR +17.56% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- INIT-EUR +15.12% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PEPE-EUR +12.08% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SHELL-EUR +10.70% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GROVE-EUR +9.20% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CSPR-EUR +9.08% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PUFFER-EUR +8.34% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
