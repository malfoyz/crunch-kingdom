const path = require('path');

module.exports = {
    module: {
      rules: [
        {
          test: /\.js$/,
          exclude: /node_modules/,
          use: {
            loader: "babel-loader"
          }
        },
        {
          test: /\.(scss|sass)$/,
          use: [
            "style-loader",
            "css-loader",
            "sass-loader",
          ],
      },
      ]
    },
  }

// module.exports = {
//   mode: 'development',
//   entry: './src/main.js',
//   output: {
//     filename: '[name].js',
//     path: path.resolve(__dirname, 'static/frontend'),
//     publicPath: '/static/frontend',
//   },
//   devServer: {
//     compress: true,
//     port: 9000,
//   },
//   module: {
//     rules: [
//       {
//         test: /\.(js|jsx)$/,
//         exclude: /node_modules/,
//         use: {
//           loader: "babel-loader",
//           options: {
//             presets: ['@babel/preset-env', '@babel/preset-react'],
//           },
//         }
//       }
//     ]
//   },
// };

// const HtmlWebpackPlugin = require('html-webpack-plugin');

// module.exports = {
//   mode: 'development',
//   entry: {
//     index: './src/main.js',
//   },
//   devtool: 'inline-source-map',
//   output: {
//     filename: '[name].js',
//     path: path.resolve(__dirname, 'static/frontend/js'),
//     publicPath: '/static/frontend/js',
//   },
//   devServer: {
//     static: './static/frontend',
//   },
//   plugins: [
//     new HtmlWebpackPlugin({
//       title: 'Development',
//     }),
//   ],
//   optimization: {
//     runtimeChunk: 'single',
//   },
//   module: {
//     rules: [
//       {
//         test: /\.(js|jsx)$/,
//         exclude: /node_modules/,
//         use: {
//           loader: "babel-loader",
//           options: {
//             presets: ['@babel/preset-env', '@babel/preset-react'],
//           },
//         }
//       }
//     ]
//   },
// };