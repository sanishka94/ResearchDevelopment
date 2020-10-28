<?php

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

// Route::get('/post/{post}', function($post) {
//     $posts = [
//         'first' => 'This is the first',
//         'second' => 'This is the second'
//     ];

//     if (! array_key_exists($post, $posts)){
//         abort(404, 'Sorry, that post does not exist');
//     }

//     return view('post', [
//         'post' => $posts[$post]
//     ]);
// });

Route::get('/post/{post}', 'PostsController@show');
