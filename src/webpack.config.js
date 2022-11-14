module.exports = {
    module: {
      rules: [
        './style',
        {
          test: /\.s[ac]ss$/i,
          use: ['style-loader', 'css-loader', 'sass-loader']
        }
      ]
    }
  }