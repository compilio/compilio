let prod = process.env.NODE_ENV === 'production'

import ExtractTextPlugin from 'extract-text-webpack-plugin'
import path from 'path'

export default {
  entry: {
    main: path.join(__dirname, '/compilio/static/js/main.js'),
    drop: path.join(__dirname, '/compilio/static/js/drop.js')
  },
  output: {
    filename: 'js/[name].js',
    path: path.join(__dirname, '/compilio/static/assets/'),
    publicPath: '/assets/'
  },
  module: {
    loaders: [
      {
        test: /\.js$/,
        loader: 'babel-loader',
        exclude: /node_modules/
      },
      {
        test: /\.css/,
        loader: ExtractTextPlugin.extract('css-loader')
      },
      {
        test: /\.vue/,
        loader: 'vue-loader'
      },
      {
        test: /\.scss$/,
        loader: ExtractTextPlugin.extract('css-loader!sass-loader')
      },
      {
        test: /\.(png|jpe?g|gif|svg|ttf|woff2?|eot)(\?.*)?$/,
        loader: 'url-loader',
        query: {
          limit: 10000,
          name: 'images/[name].[ext]'
        }
      }
    ]
  },
  plugins: [
    new ExtractTextPlugin('css/style.css')
  ],
  devServer: {
    contentBase: path.join(__dirname, '/static/assets/'),
    headers: { 'Access-Control-Allow-Origin': '*' }
  },
  devtool: prod ? false : '#inline-source-map'
}
