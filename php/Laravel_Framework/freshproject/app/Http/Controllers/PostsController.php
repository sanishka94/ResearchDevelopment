<?php

namespace App\Http\Controllers;

class PostsController
{
    public function show($post)
    {
        $posts = [
            'first' => 'This is the first',
            'second' => 'This is the second'
        ];

        if (!array_key_exists($post, $posts)) {
            abort(404, 'Sorry, that post does not exist');
        }

        return view('post', [
            'post' => $posts[$post]
        ]);
    }
}
