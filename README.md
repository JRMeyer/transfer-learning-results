# transfer-learning-results

All experiments reported here were decoded with a language model compiled into a trie via Kenlm.

The language models are pruned trigrams (i.e. singleton bigrams and trigrams removed). The training text comes from wikidumps, collected by Fran Tyers.

The models labeled `scratch` are baselines, where no transfer learning is happening - these models are trained "from scratch".

All other results represent performance from a model which was bootstrapped from the `v0.3.0` release of DeepSpeech's English checkpoints.

There were 5 transfer learning experiments per language, which involve removing layers from the English model, and reinitializing and training to the target langauge.

In these experiments, only the newly reinitialied layers are updated - the copied English layers stay frozen, acting as an non-updateable feature extractor.

The integers in the filenames indicate how many layers from the English model were removed, starting from the last layer. For example, the results in `ca/RESULTS.json.ca.2` show the decoding output of a model trained on Catalan, where the last two layers of an English model are re-initialized and trained to Catalan training data.