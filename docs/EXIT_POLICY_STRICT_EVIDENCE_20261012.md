# Audit du shadow de politiques de sortie — borne temporelle et faux `complete_horizon`

**12 octobre 2026 — recherche uniquement, PR séparée pour revue.** Aucun changement de BUY, carnet d'ordres, stop exécuté, email, portefeuille, exécution ou seuil production.

## Défaut reproduit à partir du code

Dans `scripts/update_exit_policy_shadow.py` avant cette PR :

- `_sim` et `_sim_stop_policy` prenaient les barres dont le **début** était avant `decision_ts + horizon`, même lorsque leur clôture dépassait cet horizon. Des plus-hauts ou plus-bas **post-horizon** pouvaient influencer l'issue de la simulation.
- `complete_horizon` dépendait seulement du timestamp de la **dernière barre** (proximité à moins de 10 minutes), et ne contrôlait ni les trous de données ni les doublons sur les bougies intermédiaires.
- `_summary`, `_pairwise` et `_stop_summary` admettaient ainsi les lignes où `complete_horizon=True`. Ces agrégats alimentent les comparaisons `current_tp1_stop` vs `full_1_4r/1_5r/1_6r` et le shadow de stop différé.

**Exemple conceptuel** : un signal à 10:09:52, horizon 4h à 14:09:52, ne peut pas utiliser une bougie 14:05–14:10 puisque sa clôture est après 14:09:52. Si la bougie porte une mèche cible de +20 %, c'est une fuite du futur.

## Correction proposée

- Fonction unique `_strict_price_window` commune aux politiques : bougies 5m intégralement **post-signal et clôturées avant l'horizon**, avec grille complète attendue, unicité des timestamps et absence de trous.
- `complete_horizon` ne devient `True` que si `coverage_status=COMPLETE_STRICT`. `quality_version=STRICT_CLOSED_GRID_V1` identifie la version des méthodes.
- Les comparaisons et critères de readiness n'admettent que des résultats de qualité strictement validée.
- L'ancien journal retient des `complete_horizon=True` non fiables, **exclus** des nouveaux agrégats plutôt que « certifiés » a posteriori.
- Le statut ajoute `legacy_horizon_coverage_unverified` pour afficher le nombre de lignes historiques précédemment qualifiées mais insuffisamment vérifiables.

## Impact sur les chiffres

Dernier statut pré-correction observé au **12/10 18:09:56 UTC** :

| Horizon | N dits complets (ancien calcul) | PnL net estimé baseline | PnL net estimé 1,4R |
|---|---:|---:|---:|
| 4h | 239 | −128,93 € | −28,29 € |
| 12h | 209 | −17,80 € | +85,70 € |
| 24h | 163 | +204,27 € | +112,58 € |

Ces `sum_net_pnl_eur_est` sont des **sommes de trades simulés indépendants**, sans preuve de sortie au prix du carnet, capital net ni réalité utilisateur. L'ancien contrôle de complétude ne suffit pas à les valider. **Il est impossible de connaître les nouveaux chiffres avant une réévaluation hors fuite temporelle.** Il ne faut ni attribuer ces résultats à ChatGPT, ni promouvoir le 1,4R sur ces seuls nombres.

Le shadow ne conserve pas l'ensemble des bougies historiques permettant de reconstituer toutes les anciennes trajectoires. Les lignes anciennes doivent donc rester **non vérifiées** ; ne pas leur appliquer un correctif de performance imaginé.

## Limites restantes

- Les périodes sans transaction restent des trous documentés : aucune interpolation de cours ne peut être présentée comme preuve de liquidité ou exécution.
- Le stop simulé reste une hypothèse et non un ordre Bitvavo exécuté. Les prix de sortie bid/ask et la liquidité future ne sont toujours pas démontrés.
- Comparer `N`, pertes et gains sur une même cohorte indépendante, avec budget 2 300 € et coûts ex-ante, avant une modification de stratégie.

**Tests synthétiques** : mèche post-cutoff à 4h, bougie interne manquante, timestamp dupliqué, rejet des anciens `complete_horizon=True` et comptabilité des seuls nouveaux résultats stricts.

Suivi : [issue #134](https://github.com/Vadimrom-create/bitvavo-live/issues/134). Correctif de qualité de recherche, PAS demande d'activer une nouvelle politique de sortie.
