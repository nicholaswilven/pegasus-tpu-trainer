from transformers import PegasusConfig
# Build Model using Hyperparameters, reduce to 50% from orig
def get_config(vocab_size, small=False, base=True, large=False):
    configuration = PegasusConfig()
    configuration.vocab_size = vocab_size
    if small:
        configuration.d_model = 256
        configuration.dropout = 0.2
        configuration.decoder_attention_heads = 8
        configuration.decoder_layers = 8
        configuration.decoder_ffn_dim = 2048
        configuration.encoder_attention_heads = 8
        configuration.encoder_layers = 8
        configuration.encoder_ffn_dim = 2048
    elif large:
        configuration.d_model = 1024
        configuration.dropout = 0.1
        configuration.decoder_attention_heads = 16
        configuration.decoder_layers = 16
        configuration.decoder_ffn_dim = 4096
        configuration.encoder_attention_heads = 16
        configuration.encoder_layers = 16
        configuration.encoder_ffn_dim = 4096
    elif base:
        configuration.d_model = 512
        configuration.dropout = 0.15
        configuration.decoder_attention_heads = 8
        configuration.decoder_layers = 12
        configuration.decoder_ffn_dim = 3072
        configuration.encoder_attention_heads = 8
        configuration.encoder_layers = 12
        configuration.encoder_ffn_dim = 3072
    return configuration